export default function getListStudentIds (array){
    if (!Array.isArray(array)){
        return [];
    }
    else {
        let ids = array.map((student) => student.id)
        return ids;
    }
}
