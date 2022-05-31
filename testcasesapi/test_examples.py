# package restAPI;
#
# import com.jayway.jsonpath.JsonPath;
# import io.restassured.RestAssured;
# import io.restassured.http.Method;
# import io.restassured.response.Response;
# import io.restassured.specification.RequestSpecification;
# import org.testng.Assert;
# import org.testng.annotations.Test;
#
# import java.util.Arrays;
# import java.util.List;
# import java.util.Map;
#
# import static io.restassured.RestAssured.given;
#
# /**
#  * Created by kohlih on 10-11-2017.
#  */
# public class FirstTest {
#
#     @ Test // guru99 example
#     public static void getResponseStatus(){
#     int statusCode= given().queryParam("CUSTOMER_ID", "68195")
#     .queryParam("PASSWORD", "1234!")
#     .queryParam("Account_No", "1").when().get("http://demo.guru99.com/V4/sinkministatement.php").getStatusCode();
#     System.out.println("The response status is "+statusCode);
#     // given().when().get().then().assertThat().statusCode(200);
#     }
#
#     @Test
#     public void TestCase1(){
#         Response response = given().param("q","paulo+coelho").
#                 when().get("https://www.googleapis.com/books/v1/volumes").
#                 then().statusCode(200).extract().response();
#
#         int totalItems = JsonPath.read(response.asString(),"$.totalItems");
#
#         Assert.assertTrue(totalItems>0,"Total Items should be greater than 0");
#
#         List<Map<String,Object>> allBooks = JsonPath.read(response.asString(),"$.items[*].volumeInfo");
#
#         for(Map<String,Object> book : allBooks ){
#             List<String> authors = (List<String>)book.get("authors");
#             String title=book.get("title").toString();
#
#             Assert.assertTrue(authors.contains("Paulo Coelho") || title.contains("Paulo Coelho"), "Title = " + title + " or Authors = " + Arrays.toString(authors.toArray()) + " should contain Paulo Coelho");
#         }
#     }
#
#     @Test
#     public void TestCase2(){
#         Response response = given().param("q","potter").
#                 when().get("https://www.googleapis.com/books/v1/volumes").
#                 then().statusCode(200).extract().response();
#
#         int totalItems = JsonPath.read(response.asString(),"$.totalItems");
#
#         Assert.assertTrue(totalItems>0,"Total Items should be greater than 0");
#
#         List<Object> allBooks = JsonPath.read(response.asString(),"$.items");
#
#         Assert.assertEquals(allBooks.size(),10, "10 Books should be returned by default");
#     }
#
#     @Test
#     public void TestCase3(){
#         Response response = given().param("q","dan+brown").param("maxResults","25").
#                 when().get("https://www.googleapis.com/books/v1/volumes").
#                 then().statusCode(200).extract().response();
#
#         int totalItems = JsonPath.read(response.asString(),"$.totalItems");
#
#         Assert.assertTrue(totalItems>0,"Total Items should be greater than 0");
#
#         List<Object> allBooks = JsonPath.read(response.asString(),"$.items");
#
#         Assert.assertEquals(allBooks.size(),25, "25 Books should be returned");
#     }
#
#     @Test
#     public void TestCase4(){
#         Response response = given().param("q","").
#                 when().get("https://www.googleapis.com/books/v1/volumes").
#                 then().statusCode(400).extract().response();
#
#         String errorMessage = JsonPath.read(response.asString(),"$.error.message");
#         String paramName = JsonPath.read(response.asString(),"$.error.errors[0].location");
#
#         Assert.assertTrue(errorMessage.equals("Missing query.") && paramName.equals("q"),"Search Query Parameter Missing Error should be displayed");
#     }
#
#     @Test
#     public void TestCase5(){
#         Response response = given().param("q","india").param("maxResults","50").
#                 when().get("https://www.googleapis.com/books/v1/volumes").
#                 then().statusCode(400).extract().response();
#
#         String errorMessage = JsonPath.read(response.asString(),"$.error.message");
#         String paramName = JsonPath.read(response.asString(),"$.error.errors[0].location");
#
#         Assert.assertTrue(errorMessage.contains("Values must be within the range: [0, 100]") && paramName.equals("maxResults"),"MaxResults invalid range Error should be displayed");
#     }
#     @Test
#     public void GetWeatherDetails()
#     {
#         // Specify the base URL to the RESTful web service
#         RestAssured.baseURI = "https://demoqa.com/utilities/weather/city";
#
#         // Get the RequestSpecification of the request that you want to sent
#         // to the server. The server is specified by the BaseURI that we have
#         // specified in the above step.
#         RequestSpecification httpRequest = RestAssured.given();
#
#         // Make a request to the server by specifying the method Type and the method URL.
#         // This will return the Response from the server. Store the response in a variable.
#         Response response = httpRequest.request(Method.GET, "/Hyderabad");
#
#         // Now let us print the body of the message to see what response
#         // we have recieved from the server
#         String responseBody = response.getBody().asString();
#         System.out.println("Response Body is =>  " + responseBody);
#     }
#     @Test //guru99 example
#     public static void getResponseStatus(){
#         int statusCode= given().queryParam("CUSTOMER_ID","68195")
#                 .queryParam("PASSWORD","1234!")
#                 .queryParam("Account_No","1") .when().get("http://demo.guru99.com/V4/sinkministatement.php").getStatusCode();
#         System.out.println("The response status is "+statusCode);
#         // given().when().get().then().assertThat().statusCode(200);
#     }
# }
#
