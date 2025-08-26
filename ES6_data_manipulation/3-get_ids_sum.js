function getsum(total, num){
    return total + num
}
export default function getStudentIdsSum(array){
    
   return array.reduce(getsum, 0);
} 
