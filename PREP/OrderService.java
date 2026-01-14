// Create a service class to calculate total order amount for a customer
// Input: list of order amounts
// Output: total amount
import java.util.List;
/**
 * Service class to manage customer orders.
 */
// Improve this code to handle null or empty lists

public class OrderService {
    // Improve this code to handle null or empty lists
    /**
     * Calculates the total order amount for a customer.
     *
     * @param orderAmounts List of individual order amounts.
     * @return Total order amount.
     */
    // Refactor this method using Java Streams
    public double calculateTotalOrderAmount(List<Double> orderAmounts) { // Explain what this method does
        // This method calculates the total order amount by summing up all individual order amounts.
        if (orderAmounts == null || orderAmounts.isEmpty()) {
            return 0.0;
        }
        return orderAmounts.stream().mapToDouble(Double::doubleValue).sum();
    }
}

// Write a JUnit test for calculateTotal method in OrderService class
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
/**
 * Test class for OrderService.
 */
public class OrderServiceTest {
    private OrderService orderService;
    @BeforeEach
    public void setUp() {
        orderService = new OrderService();
    }
    @Test
    public void testCalculateTotalOrderAmount() {
        List<Double> orderAmounts = Arrays.asList(100.0, 200.5, 50.25);
        double expectedTotal = 350.75;
        double actualTotal = orderService.calculateTotalOrderAmount(orderAmounts);
        assertEquals(expectedTotal, actualTotal, 0.001);
    }
}   

// Improve this code to handle null or empty lists
