import javax.crypto.Cipher;  
import javax.crypto.spec.SecretKeySpec;  
import java.nio.charset.StandardCharsets;  
import java.util.Base64;  
  
public class SecurityUtils {  
    private static final String KEY = "mysecretkey"; // 密钥  
  
    // 加密方法  
    public static String encrypt(String strToEncrypt) throws Exception {  
        Cipher cipher = Cipher.getInstance("AES");  
        SecretKeySpec secretKey = new SecretKeySpec(KEY.getBytes(StandardCharsets.UTF_8), "AES");  
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);  
        return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes(StandardCharsets.UTF_8)));  
    }  
  
    // 解密方法  
    public static String decrypt(String strToDecrypt) throws Exception {  
        Cipher cipher = Cipher.getInstance("AES");  
        SecretKeySpec secretKey = new SecretKeySpec(KEY.getBytes(StandardCharsets.UTF_8), "AES");  
        cipher.init(Cipher.DECRYPT_MODE, secretKey);  
        return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));  
    }  
}
