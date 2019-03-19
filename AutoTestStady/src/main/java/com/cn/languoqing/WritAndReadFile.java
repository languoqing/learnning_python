package com.cn.languoqing;


import java.io.*;

public class WritAndReadFile {

    File file = new File("C:\\Users\\ex-languoqing600\\Desktop\\demmo.java");
    File infile = new File("D:\\gitDir\\AutoTestStady\\src\\files\\test");

    public void readFile(File f) throws FileNotFoundException{
        FileInputStream fhdle = new FileInputStream(f);
        try{
        while(fhdle.read() != -1) {
                System.out.println((char) fhdle.read());
            }
        System.out.println("读取完毕");

        }catch(Exception e){
            System.out.println(e);
        }
        finally {
            try{
                fhdle.close();
            }catch (Exception e){
                System.out.println(e);
            }
        }
    }

    public String readByteFile(File f) throws FileNotFoundException{
        byte[] b = new byte[1024];
        String restr = new String();
        FileInputStream fl = new FileInputStream(f);
        try {
            int n = 0;
            while ((n=fl.read(b)) != -1){
                String str = new String(b,0,n);
                //System.out.println(str);
                restr = str;

            }
        }catch (Exception e){
            System.out.println(e);
        }
        finally {
            try{
                fl.close();
            }catch (Exception e){
                System.out.println(e);
            }
        }
        return restr;
    }

    /**
     * 写入文件操作
     * @param f;
     */
    public void writeFile(File f) throws FileNotFoundException{
        FileOutputStream fos = new FileOutputStream(f,true);
        try{
            fos.write('b');
            fos.write('a');
        }catch (IOException e){
            System.out.println(e);
        }
        finally {
            try{
                fos.close();
            }catch (IOException e){
                System.out.println(e);
            }

        }

    }

    /**
     *  写入文件操作，byte[]，讲读取的file文件，再写入到infile
     * @param f:要读写的文件地址
     */

    public void writeByteFile(File f) throws FileNotFoundException{
        byte[] b = readByteFile(file).getBytes();
        System.out.println("+++++++"+b);
        FileOutputStream fos = new FileOutputStream(f);
        try{
            fos.write(b);
        }catch (IOException e){
            System.out.println(e);
        }
        finally {
            try {
                fos.close();
            }catch (IOException e){
                System.out.println(e);
            }
        }

    }

    public static void main(String[] args){
        WritAndReadFile obj = new WritAndReadFile();
        try{
            //obj.readFile(obj.file);
            String a = obj.readByteFile(obj.file);
            System.out.println("===================");
            System.out.println(a);
        }catch (Exception e){
           System.out.println(e);
        }

        try{
            obj.writeFile(obj.infile);
        }catch (FileNotFoundException e){
            System.out.println(e);
        }

        try{
            obj.writeByteFile(obj.infile);
        }catch (FileNotFoundException e){
            System.out.println(e);
        }

    }
}
