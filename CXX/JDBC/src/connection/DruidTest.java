package connection;

import java.io.InputStream;
import java.sql.Connection;
import java.util.Properties;

import javax.sql.DataSource;

import com.alibaba.druid.pool.DruidDataSourceFactory;
import org.junit.Test;


public class DruidTest {
	
	@Test
	public void getConnection() throws Exception{
		Properties pros = new Properties();
		
		InputStream is = ClassLoader.getSystemClassLoader().getResourceAsStream("druid.properties");
		
		pros.load(is);
		
		DataSource source = DruidDataSourceFactory.createDataSource(pros);
		Connection conn = source.getConnection();
		System.out.println(conn);
		
	}
}
