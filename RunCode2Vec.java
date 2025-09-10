import java.io.File;
import java.io.IOException;

public class RunCode2Vec {
    public static void main(String[] args) {
        String jarPath = "E:\\github\\EmbeddedKittens\\target\\embedded-kittens-1.0.full.jar";
        // 地址是 E:\\dataset\\anonymizeddata\\data\\hoc18\\scripts\\
        String outputPath = "E:\\dataset\\anonymizeddata\\data\\hoc18\\code2seq16\\";
        // 地址是 E:\\dataset\\anonymizeddata\\data\\hoc18\\scripts\\
        String projectPath = "E:\\dataset\\anonymizeddata\\data\\hoc18\\trace\\";

        // 创建输出目录（如果不存在）
        File outputDir = new File(outputPath);
        if (!outputDir.exists()) {
            outputDir.mkdirs();
        }

        // 遍历 projectPath 下的所有文件，使用 ProcessBuilder 处理每个文件
        File folder = new File(projectPath);
        File[] listOfFiles = folder.listFiles();

        if (listOfFiles != null) {
           // int counter = 1;
            for (File file : listOfFiles) {
                if (file.isFile()) {
                    // 对文件进行 ProcessBuilder 处理
                    ProcessBuilder processBuilder = new ProcessBuilder(
                        "java", "-jar", jarPath, "code2seq",
                        "--output", outputPath,
                        "--path", file.getAbsolutePath(),
                        "--whole-program", "--max-path-length=16"
                    );

                    processBuilder.redirectErrorStream(true);

                    try {
                        Process process = processBuilder.start();
                        int exitCode = process.waitFor();

                        if (exitCode == 0) {
                            System.out.println("处理成功：" + file.getName());
                        } else {
                            System.out.println("处理失败：" + file.getName());
                        }
                    } catch (IOException | InterruptedException e) {
                        e.printStackTrace();
                    }

                //    counter++;
                }
            }
        } else {
            System.out.println("文件夹不存在或为空：" + projectPath);
        }
    }
}