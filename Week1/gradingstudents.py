
class gradesyystem(object):
    def gradingsystem(self,grade):
        grades=[]
        for i in range(grade):
            if grade>40 and grade<45:
                nexts=45
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>45 and grade<50:
                nexts=50
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>50 and grade<55:
                nexts=55
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>55 and grade<60:
                nexts=60
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>60 and grade<65:
                nexts=65
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>65 and grade<70:
                nexts=70
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>70 and grade<75:
                nexts=75
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>75 and grade<80:
                nexts=80
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>80 and grade<85:
                nexts=85
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>85 and grade<90:
                nexts=90
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>90 and grade<95:
                nexts=95
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            elif grade>95 and grade<100:
                nexts=100
                if nexts-grade<3:
                    grade=nexts
                    grades.append(grade)
                    break
                else:
                    grades.append(grade)
                    break
            else:
                grades.append(grade)
                break
        print (grades)
            

                