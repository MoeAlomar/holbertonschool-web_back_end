export default function hasValuesFromArray(set, array){
    for (let i = 0; i < array.length; i++){
        if (!set.has(arr[i])){
            return false;
        }
    }
    return true;
}
