class StudentManagement:
    def __init__(self):
        self.students = {}

    def accept(self, name, roll, marks1, marks2):
        self.students[roll] = [name, roll, marks1, marks2]

    def display(self):
        print("Student Details:")
        for roll, values in self.students.items():
            print(f"Student roll: {values[1]}")
            print(f"Student name: {values[0]}")
            print(f"Mark1: {values[2]}")
            print(f"Mark2: {values[3]}")

    def search(self, roll):
        if roll in self.students:
            values = self.students[roll]
            print(f"Student roll: {values[1]}")
            print(f"Student name: {values[0]}")
            print(f"Mark1: {values[2]}")
            print(f"Mark2: {values[3]}")
        else:
            print(f"Student with roll number {roll} not found.")


st = StudentManagement()

st.accept("Rahim", 1, 70, 80)
st.accept("Fahim", 2, 78, 60)
st.accept("Mahim", 3, 66, 83)
st.accept("Zahim", 4, 71, 86)
st.accept("Tahim", 5, 77, 92)

st.display()

st.search(4)
st.search(6)