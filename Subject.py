class Chapter:
    """
    Stores information about the position of each topic and dinamically updates after changes occurr
    """
    name: str
    theory_pages: dict = {"topic": "position"}
    excercise_pages: dict = {"topic": {"name" : "position"}}

    def __init__(self, name:str):
        self.name=name



    def Add_page(self, topic:str, position:str, excercise:bool):

        page: dict = {topic, position}
        if excercise:
            self.excercise_pages += page
        else:
            self.theory_pages += page

    def Get_theory(self, topic:str):
        """ 
        Takes a topic and returns the position of the corresponding page 
        """
        return self.theory_pages[topic]

    

        

class Subject:
    name: str
    chapters: dict = {"chapter" : Chapter("chapter")}

    def Add_chapter(self, chapter: Chapter):
        holder: dict = {chapter.name : chapter}
        self.chapters += holder

trial = Chapter(name="Thermodynamics")
print(trial.name)
print(trial.excercise_pages)
print(trial.theory_pages)
