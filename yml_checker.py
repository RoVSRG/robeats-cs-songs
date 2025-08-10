import yaml
import os
import shutil

class MapCheck():
    def __init__(self, songName, metadataPath, basePath):
        self.songName = songName
        self.metadataPath = metadataPath
        self.basePath = basePath

    def modifyYml(self):
        with open(f"{self.metadataPath}", "r", encoding="utf-8") as song:
            try:
                yamlData = yaml.safe_load(song)
                filterDifficultyData = [i for i in yamlData.get("Difficulty") if i.get("Rate") == 100]
            except Exception:
                print("Error Reading")
                
        yamlData["Difficulty"] = filterDifficultyData

        with open(f"{self.metadataPath}", "w", encoding="utf-8") as song:
            try:
                yaml.dump(yamlData, song, sort_keys=False)
                print(f"{self.metadataPath} has been modified.")

            except Exception:
                print("Error Writing")

    def removeCharterFiles(self):
        try:
            with open(f"{self.metadataPath}", "r", encoding="utf-8") as song:
                yamlData = yaml.safe_load(song)

            if yamlData.get("Mapper") in ["YasiCreeper", "Yasi"]:
                os.chmod(self.basePath, 0o777)
                shutil.rmtree(self.basePath)
                print(f"{self.basePath} has been removed.")

        except Exception as err:
            print(err)
            print("There was an error deleting the mapper's charts!")

def getPath():
    relativeDirectory = os.getcwd()
    newPath = os.chdir(relativeDirectory + r"\songs")
    return newPath

def main():
    songNames = os.listdir(getPath())
    for i in range(len(songNames)):
        basePath = os.path.join(os.getcwd(), songNames[i])
        metadataPath = basePath + r"\metadata.yml"

        try:
            checkDatMf = MapCheck(songNames[i], metadataPath, basePath)
            #checkDatMf.modifyYml()
            checkDatMf.removeCharterFiles()
        except Exception as err:
            print(err)

if __name__ == "__main__":
    main()


