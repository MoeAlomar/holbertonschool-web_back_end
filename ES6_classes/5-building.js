export default class Building {
    constructor(sqft) {
      // Store in underscore attribute version
      this._sqft = sqft;
      
      // Only check for abstract method implementation if this is a subclass
      if (this.constructor !== Building) {
        // Check if extending class implements required abstract method
        if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
          throw new Error('Class extending Building must override evacuationWarningMessage');
        }
      }
    }
  
    // ES6 Getter for sqft attribute
    get sqft() {
      return this._sqft;
    }
  
    // Abstract method that must be overridden by subclasses
    evacuationWarningMessage() {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
