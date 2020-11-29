Date.prototype.getWeek = function () {
    let tdt = new Date(this.valueOf());
    let dayn = (this.getDay() + 6) % 7;
    tdt.setDate(tdt.getDate() - dayn + 3);
    let firstThursday = tdt.valueOf();
    tdt.setMonth(0, 1);
    if (tdt.getDay() !== 4) {
        tdt.setMonth(0, 1 + ((4 - tdt.getDay()) + 7) % 7);
    }

    let week = 1 + Math.ceil((firstThursday - tdt) / 604800000)
    return week > 52 ? 1 : week;
}