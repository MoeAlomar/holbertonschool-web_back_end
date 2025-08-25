class Student {
    constructor(id, firstName, location){
    }
}
s1 = new Student(1, "Guillaume", "San Fransisco")
s2 = new Student(2, "James", "Colombia")
s3 = new Student(5, "Serena", "San Fransisco")
export default function getListStudents(){
    return [s1, s2, s3]
}
