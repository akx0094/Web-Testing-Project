import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class FormSubmissionTest {
    public static void main(String[] args) {
        // Set the path to your ChromeDriver
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");

        WebDriver driver = new ChromeDriver();

        try {
            // Open your web page
            driver.get("http://localhost/Final/connect.php");

            // Set an implicit wait
            driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));

            // Wait for the input fields to be present
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));
            WebElement nameField = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("name")));
            WebElement emailField = driver.findElement(By.name("email"));
            WebElement messageField = driver.findElement(By.name("message"));

            // Input test data
            nameField.sendKeys("John Doe");
            emailField.sendKeys("john@example.com");
            messageField.sendKeys("Hello, this is a test message!");

            // Submit the form
            WebElement submitButton = driver.findElement(By.name("submit"));
            submitButton.click();

            // Wait for a success message or the next page
            WebElement successMessage = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//body")));
            System.out.println("Response: " + successMessage.getText());

        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        } finally {
            // Close the browser
            driver.quit();
        }
    }
}
