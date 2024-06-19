import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;
import java.util.Map;

/**
 * http����
 * @author 32249
 * @ֱ��ʹ��ѵ���õ�DNN����ģ�����ж�
 */
public class HttpUtil {
	// ��������
	/*
	 * @������Ϣ
	 * @return ���
	 * 
	 * */
    public static String post(String requestUrl, String accessToken, String params)
            throws Exception 
    {
    	//����contentType
        String contentType = "application/x-www-form-urlencoded";
        return HttpUtil.post(requestUrl, accessToken, contentType, params);
    }
 
    
    
    public static String post(String requestUrl, String accessToken, String contentType, String params)
            throws Exception
    {
    	//���ñ����ʽΪUTF-8
        String encoding = "UTF-8";
        if (requestUrl.contains("nlp")) 
        {
        	//�����ʹ��NLP����Ҫʹ��GBK���룬����ǰٶ�api�Ǳ���Ҫ���
            encoding = "GBK";
        }
        //����
        return HttpUtil.post(requestUrl, accessToken, contentType, params, encoding);
    }
 
    public static String postGeneralUrl(String generalUrl, String contentType, String params, String encoding)
            throws Exception 
    {
    	//����URL
        URL url = new URL(generalUrl);
        //����HttpURLConnection
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        //����Content-Type
        connection.setRequestProperty("Content-Type", contentType);
        //����������Ϣ
        connection.setRequestProperty("Connection", "Keep-Alive");
        connection.setUseCaches(false);
 
        connection.setDoOutput(true);
        connection.setDoInput(true);
        //����������������
        DataOutputStream out = new DataOutputStream(connection.getOutputStream());
        out.write(params.getBytes(encoding));
        out.flush();
        //�ر�
        out.close();
        //����
        connection.connect();
        //�������ͷ��ӡ����
        Map<String, List<String>> headers = connection.getHeaderFields();
        for (String key : headers.keySet()) {
            System.err.println(key + "--->" + headers.get(key));
        }
        
        BufferedReader in = null;
        //�õ����
        in = new BufferedReader(new InputStreamReader(connection.getInputStream(), encoding));
        String result = "";
        String getLine;
        //�����ȡ����
        while ((getLine = in.readLine()) != null) {
            result += getLine;
        }
        in.close();
        //�������ӡ���������ؽ��
        System.err.println("result:" + result);
        //���ؽ��
        return result;
    }
    
    /*
     * @
     * 
     * */
    public static String post(String requestUrl, String accessToken, String contentType, String params, String encoding)
            throws Exception {
    	//��������url����������Ϣд��url��
        String url = requestUrl + "?access_token=" + accessToken;
        //����
        return HttpUtil.postGeneralUrl(url, contentType, params, encoding);
    }
