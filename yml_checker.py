import yaml
import os

class MapCheck():
    def __init__(self, songName, metadataPath):
        self.songName = songName
        self.metadataPath = metadataPath

    def modifyYml(self):
        with open(f"{self.metadataPath}", "r", encoding="utf-8") as song:
            try:
                yamlData = yaml.safe_load(song)
                filterDifficultyData = [i for i in yamlData["Difficulty"] if i["Rate"] == 100]
            except Exception:
                print("Error Reading")
        yamlData["Difficulty"] = filterDifficultyData

        with open(f"{self.metadataPath}", "w", encoding="utf-8") as song:
            try:
                yaml.dump(yamlData, song, sort_keys=False)
            except Exception:
                print("Error Writing")

def getPath():
    relativeDirectory = os.getcwd()
    newPath = os.chdir(relativeDirectory + r"\songs")
    return newPath

def main():
    songNames = os.listdir(getPath())
    for i in range(len(songNames)):
        metadataPath = os.path.join(os.getcwd(), songNames[i]) + r"\metadata.yml"

        # songMetaData = [j for j in os.scandir(songNames[i]) 
        #                 if j.name.endswith("metadata.yml")]
        # print(f"{songNames[i]} - {songMetaData}")

        try:
            checkDatMf = MapCheck(songNames[i], metadataPath)
            checkDatMf.modifyYml()
            print(f"{songNames[i]} has been modified.")

        except Exception as err:
            print(err)

if __name__ == "__main__":
    main()


