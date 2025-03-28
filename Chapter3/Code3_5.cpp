    #include <iostream>
}
￼
class Operations: public vector {
￼
private: 
    double x1, y1, z1, x2, y2, z2;
￼
public:
￼
    Operations();
    Operations(double a, double b, double c, double aa, double bb, double cc) {
        x1 = a;
        y1 = b;
        z1 = c;
        x2 = a;
        y2 = b;
        z2 = c;
    }
￼
    void SetVector1(double a, double b, double c) {
        x1 = a;
        y1 = b;
        z1 = c;
    }
    void SetVector2(double aa, double bb, double cc) {
        x2 = aa;
        y2 = bb;
        z2 = cc;
    }
    void SetVectors(double a, double b, double c, double aa, double bb, double cc) {
        x1 = a;
        y1 = b;
        z1 = c;
        x2 = a;
        y2 = b;
        z2 = c;
    }
￼
    void Sum() {
        x = x1 + x2;
        y = y1 + y2;
        z = z1 + z2;
    }
};
￼
Operations::Operations() {
    cout << "Hello" << endl;
}
￼
int main() {
￼
    double n, m, s;
￼
    cin >> n >> m >> s;
￼
    vector pino(n, m, s);
    cin >> n >> m >> s;
￼
    vector pina(n, m, s);
￼
    Operations test(n, m, n, m, n, s);
    test.Sum();
    cout << test.GetTheta() << endl;
￼
    n = 10;
￼
    return 0;
}
