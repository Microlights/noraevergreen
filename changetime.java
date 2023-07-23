import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateConverter {
    public static void main(String[] args) {
        // 输入日期字符串和当前格式
        String dateString = "2021-01-31";
        String currentFormat = "yyyy-MM-dd";

        // 目标日期格式
        String targetFormat = "dd/MM/yyyy";

        // 创建当前格式的日期解析器和目标格式的日期格式化器
        DateTimeFormatter currentFormatter = DateTimeFormatter.ofPattern(currentFormat);
        DateTimeFormatter targetFormatter = DateTimeFormatter.ofPattern(targetFormat);

        try {
            // 解析当前格式的日期字符串
            LocalDate date = LocalDate.parse(dateString, currentFormatter);

            // 格式化日期为目标格式
            String formattedDate = date.format(targetFormatter);

            // 输出结果
            System.out.println("转换结果: " + formattedDate);
        } catch (Exception e) {
            System.out.println("日期转换出错: " + e.getMessage());
        }
    }
}
