class School:
    def __init__(self,school_name):
        self.school_name = school_name
        self.roster = {}

    def get_roster(self):
        return self.roster

#You should be able to add a student to the school by calling the add_student method and giving it an argument of the student's name and their grade.

    def add_student(self,student_name,grade):
        if grade in self.roster:
            self.roster[grade].append(student_name)
        else:
            self.roster[grade] = []
            self.roster[grade].append(student_name)
        return sorted(self.roster)
                                      
#Next, define a method called grade, which should take in an argument of a grade and return a list of all the students in that grade:

    def grade(self, grade):
        return self.roster[grade]
    
#Define a method called sort_roster that returns the school's roster where the strings in the student arrays are sorted alphabetically. For instance: {9: ["Kelly Slater"], 10: ["Ryan Sheckler", "Tony Hawk"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}}

    def sort_roster(self):
        for grade in self.roster:
            self.roster[grade].sort()
        return self.roster