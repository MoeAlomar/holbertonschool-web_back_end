export default function getStudentsByLocation(array, city){
    if(Array.isArray(array) && typeof city === "string"){
        return array.filter((student) => student.location === city);
    }
    else 
    return [];

}
