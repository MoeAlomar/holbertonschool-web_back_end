export default function getFullResponseFromAPI(success){
    return new Promise((resolve, reject) => {   
    if (sucess){
        return resolve({
            "status": 200,
            "body": "sucess",
        });
    
    }
    else{
        return reject("The fake API is not working currently")
    }
    });
}
