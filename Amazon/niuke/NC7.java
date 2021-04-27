import java.util.*;
import java.lang.Math.*;

public class Solution {
    /**
     * 
     * @param prices int整型一维数组 
     * @return int整型
     */
    public int maxProfit (int[] prices) {
        if (prices.length <= 1){
            return 0;
        }
        int price = prices[0];
        int profit = prices[1] - prices[0];
        for (int i =1;i < prices.length;i++){
            price = Math.min(price, prices[i]);
            profit = Math.max(profit, prices[i]- price);
        }
        return profit;
    }
}