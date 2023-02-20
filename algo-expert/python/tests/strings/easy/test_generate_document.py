from algo_expert.strings.easy.generate_document import generate_document


class TestGenerateDocument:
    def test_case_0(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"

        expected = True

        assert generate_document(characters, document) == expected
