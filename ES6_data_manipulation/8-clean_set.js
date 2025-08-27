export default function cleanSet(set, startString) {
    if (!startString || typeof startString !== "string") {
        return '';
    }
    let result = [];
  
    for (let value of set) {
      if (value.startsWith(startString)) {
        result.push(value.slice(startString.length));
      }
    }
  
    return result.join('-');
  }
  