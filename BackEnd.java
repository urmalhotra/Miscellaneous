import java.util.Arrays;
import java.util.*;
public class BackEnd {
    public static double[] calculatingx(double[] inputx, double[] inputy) {
        double sum = 0.0;
        int ctrl = 1;
        double tempx = 0.0;
        double tempy = 0.0;
        double val = Math.sqrt(((inputx[0] - inputx[1]) * (inputx[0] - inputx[1]))
            + ((inputy[0] - inputy[1]) * (inputy[0] - inputy[1])));
        for (int i = 0; i < 2; i++) {
            ctrl = 1;
            while (ctrl + i < 3) {
                sum = Math.sqrt(((inputx[i] - inputx[i + ctrl]) * (inputx[i] - inputx[i + ctrl]))
                    + ((inputy[i] - inputy[i + ctrl]) * (inputy[i] - inputy[i + ctrl])));
                if (sum <= val) {
                    val = sum;
                    tempx = inputx[i];
                    inputx[i] = inputx[ctrl + i];
                    inputx[i + ctrl] = tempx;
                    tempy = inputy[i];
                    inputy[i] = inputy[ctrl + i];
                    inputy[i + ctrl] = tempy;
                }
                ++ctrl;
            }
        }
        return inputx;
    }
    public static double[] calculatingy(double[] inputx, double[] inputy) {
        double sum = 0.0;
        int ctrl = 1;
        double tempx = 0.0;
        double tempy = 0.0;
        double val = Math.sqrt(((inputx[0] - inputx[1]) * (inputx[0] - inputx[1])) + ((inputy[0] - inputy[1]) * (inputy[0] - inputy[1])));
        for (int i = 0; i < 2; i++) {
            ctrl = 1;
            while (ctrl + i < 3) {
                sum = Math.sqrt(((inputx[i] - inputx[i + ctrl]) * (inputx[i] - inputx[i + ctrl])) + ((inputy[i] - inputy[i + ctrl]) * (inputy[i] - inputy[i + ctrl])));
                if (sum <= val)
                {
                    val = sum;
                    tempx = inputx[i];
                    inputx[i] = inputx[ctrl + i];
                    inputx[i + ctrl] = tempx;
                    tempy = inputy[i];
                    inputy[i] = inputy[ctrl + i];
                    inputy[i + ctrl] = tempy;
                }
              ++ctrl;
            }
        }
        return inputy;
    }
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double[] inputx = new double[3];
        double[] inputy = new double[3];
        double[] finalx = new double[3];
        double[] finaly = new double[3];
        finalx = calculatingx(inputx, inputy);
        finaly = calculatingy(inputx, inputy);
        System.out.println(Arrays.toString(finalx));
        System.out.println(Arrays.toString(finaly));
    }
}


