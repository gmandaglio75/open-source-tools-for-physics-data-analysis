   #include <iostream>
        }
        double showHistogram(int position)  // Method to display a bin
        {
            return *(histogram + position - 1);
        } 
};
￼
data::data(double *array, int index)  // Constructor with input of an array and its size
{
    this->index = index;
    vector = new double[index];
    for (int i = 0; i < index; i++) {  // Load the array into the class
        *(vector + i) = array[i];
    }
}
￼
data::data(string name)
{
    index = 0;
    double temp;
    ifstream readFile(name.c_str());
    if (!readFile.good()) {
        cout << "Error! File not found." << endl;
    }
    while(!readFile.eof()) {
        readFile >> temp;
        if(!readFile.eof()) {
            index++;
        }
    }
    vector = (double *)malloc(index * sizeof(double));
    readFile.close();
    readFile.open(name.c_str());
    for (int i = 0; i < index; i++) {
        readFile >> *(vector + i);
    }
    readFile.close();
}
￼
int main()
{
    int intervals;
    char response;
    string filename;
    cout << "Which file would you like to load data from? Enter the name with extension (e.g., data.dat): ";
    cin >> filename;
    data histogram(filename);
    cout << "The maximum value is: " << histogram.getMax() << endl;
    cout << "The minimum value is: " << histogram.getMin() << endl;
    cout << "The mean value is: " << histogram.getMean() << endl;
    cout << "The standard deviation is: " << histogram.getStdDev() << endl;
    cout << "The standard error of the mean is: " << histogram.getMeanDev() << endl;
    cout << "Would you like to create a histogram? (Yes=Y, No=N)" << endl;
    cin >> response;
    if(response == 'Y' || response == 'y') {
        cout << "Into how many intervals would you like to divide the data?" << endl;
        cin >> intervals;
        histogram.createHistogram(intervals);
        for (int i = 1; i <= intervals; i++) {
            cout << "Bin number " << i << " contains " << histogram.showHistogram(i) << " elements." << endl;
        }
    }
    system("PAUSE");  // Command for Windows cmd.exe console
    return 0;
}
