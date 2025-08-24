import Building from "./5-building.js";
export default class SkyHighBuilding extends Building{
    constructor(sqft, floors){
        Building._sqft = sqft;
        this._floors = floors;

    }

    get sqft(){
        return  Building._sqft;
    }
    get floors(){
        return this._floors;
    }
    evacuationWarningMessage(){
        return `Evacuate slowly the ${this._floors} floors`
    }
}
