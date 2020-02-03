
class RUN:
    def runAll(self):
        from FinalDataset.DiseaseSymptomDictionary import DisSym
        d=DisSym()
        d.DiseaseSymptomD()

        from FinalDataset.Rough1 import rough1
        r1=rough1()
        r1.runRough1()

        from FinalDataset.Rough2 import rough2
        r2=rough2()
        r2.runRough2()

        from FinalDataset.ValueDiseaseTagging import ValDisTag
        v=ValDisTag()
        v.valueDisease()


r=RUN().runAll()