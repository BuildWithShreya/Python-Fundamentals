# module(college_name)
import college
def main():
    college_name= college.ask_college()
    college.display_college(college_name)
if __name__ == "__main__":
    main()