from typing import Dict
import pickle


class DifferenceScores:
    __score_matrix: Dict[str, Dict[str, float]]

    def __init__(self):
        self.__score_matrix = dict()

    def set_score(self, entity1: str, entity2: str, score: float):
        """Sets the difference score between a pair of entities.
        :param entity1: The first entity.
        :param entity2: The second entity.
        :param score: The difference score between entity1 and entity2."""

        if entity1 > entity2:
            entity1, entity2 = entity2, entity1

        if entity1 not in self.__score_matrix:
            self.__score_matrix[entity1] = dict()

        if entity2 not in self.__score_matrix:
            self.__score_matrix[entity2] = dict()

        self.__score_matrix[entity1][entity2] = score

    def get_score(self, entity1: str, entity2: str):
        """Gets the score between a pair of entities, if it exists.
        :param entity1: The first entity.
        :param entity2: The second entity.
        :return: The difference score between the entities. If none exists, returns None."""

        if entity1 == entity2:
            return 0.0
        elif entity1 > entity2:
            entity1, entity2 = entity2, entity1

        if self.__score_matrix[entity1] and self.__score_matrix[entity1][entity2] is not None:
            return self.__score_matrix[entity1][entity2]
        else:
            return None

    def normalize(self, print_extremes=False):
        """ Normalizes all the difference scores, so that the two most different entities have a score of 1.
        :param print_extremes: If True, prints the names of the two most different entities."""

        max_diff, max_c1, max_c2 = -999, "", ""

        entities = list(self.__score_matrix.keys())
        print("ents:", entities)
        for i1, e1 in enumerate(entities):
            entities_left = entities[i1 + 1:]
            for i2, e2 in enumerate(entities_left):
                diff_score = self.get_score(e1, e2)

                print(e1, e2, diff_score)

                if diff_score > max_diff:
                    max_diff, max_c1, max_c2 = diff_score, e1, e2
                    print(f"New most different: ({max_c1}, {max_c2}) = {max_diff}")

        if print_extremes:
            print(f"Most Different Entities: ({max_c1}, {max_c2}) = {max_diff}")

        for i1, e1 in enumerate(entities):
            entities_left = entities[i1 + 1:]
            for i2, e2 in enumerate(entities_left):
                diff_score = self.get_score(e1, e2)
                self.set_score(e1, e2, diff_score / max_diff)

    def get_entity_names(self):
        """:return: A list of all entity names in this object"""
        return list(self.__score_matrix.keys())

    def save_as(self, file_loc: str):
        """Saves the DifferenceScores object to the specified file
        :param file_loc: The file to save the DifferenceScores object to"""

        with open(file_loc, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_from_file(file_loc: str):
        """Loads a DifferenceScores object from the specified file
        :param file_loc: The file to load the DifferenceScores object from
        :return: A DifferenceScores object."""

        with open(file_loc, "rb") as f:
            data: DifferenceScores = pickle.load(f)
            return data

    def print_as_matrix(self, file_loc: str):
        """Prints all the difference scores between all entities to a specified file.
        :param file_loc: The location to print the matrix to."""

        output_txt = ""

        # Create Header line
        output_txt += "Entity"
        for e in self.__score_matrix:
            output_txt += "\t" + e
        output_txt += "\n"

        for e1 in self.__score_matrix:
            output_txt += e1
            for e2 in self.__score_matrix:
                diff_score = self.get_score(e1, e2)
                output_txt += "\t" + str(diff_score)
            output_txt += "\n"

        with open(file_loc, "w") as f:
            f.write(output_txt)
