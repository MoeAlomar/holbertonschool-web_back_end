function getsum(total, num){
    return total + num;
}

export default function getStudentIdsSum(array){
    const ids = array.map((student) => student.id);
    return ids.reduce(getsum, 0);
}
