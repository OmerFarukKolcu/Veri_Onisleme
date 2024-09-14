Projede kullanılan yöntem, donanımlar ve yazılımlar:\n
Python programlama dili üzerinde :
Pandas: Veri işlemesi ve analizi için oluşturulmuş python programlama dili kütüphanesi.
Numpy: Python programlama dili için büyük, çok boyutlu dizileri ve matrisleri destekleyen, bu diziler üzerinde çalışacak üst düzey matematiksel işlevler ekleyen bir kitaplıktır.
PyQt5:Python eklentisi olarak uygulanan, platformlar arası GUI araç seti Qt'nin bir Python bağlantısıdır.
Tkinter: Python ile görsel programlama yapmamızı sağlayan kütüphanedir.
Os: Python'da hazır olarak gelen , dosya ve dizinlerde kolaylıkla işlemler yapmamızı sağlayan bir modüldür.
 Sys: Python sürümü ile ilgili bilgi edinmenizi ve kullandığınız Python sürümü ile çeşitli işlemler yapabilmenizi sağlar.
String: Listeleri işlemek için ek araçlar sağlar. Standart veri yapısında bulunan bazı yöntemler, dizi modülünde mevcut değildir.
Pathlib: Dosyalar ve dizinlerle çalışmak için bir nesne API'si sağlayan standart bir Python modülü.
Matplotlib: Matplotlib, Python'da statik, hareketli ve etkileşimli görselleştirmeler oluşturmak için kapsamlı bir kitaplıktır. Matplotlib kolay şeyleri kolay, zor şeyleri mümkün kılar.
CSV: Sözde CSV (Virgülle Ayrılmış Değerler) formatı, elektronik tablolar ve veritabanları için en yaygın içe ve dışa aktarma formatıdır. CSV formatı, formatı RFC 4180'de standart bir şekilde tanımlama girişimlerinden önce uzun yıllar kullanıldı.
Math: Bu modül, C standardı tarafından tanımlanan matematiksel fonksiyonlara erişim sağlar.
Scipy: SciPy, Python’un Numpy uzantısına dayanan matematiksel algoritmalar ve kolaylık işlevlerinin bir koleksiyonudur.
Sklearn: Scikit-learn, Python'da makine öğrenimi için muhtemelen en kullanışlı kütüphanedir. Sklearn kitaplığı, sınıflandırma, regresyon, kümeleme ve boyut azaltma dahil olmak üzere makine öğrenimi ve istatistiksel modelleme için birçok verimli araç içerir.

Özgün Değer
 Veri setindeki var olan verilerin yorumlanması çok fazla verinin bulunduğu veri setlerinde inceleme veya işlem yapmak hesap makinesi yardımı ile çok zor olmaktadır. Veri ön işleme yöntemleri sayesinde veri seti üzerinde daha hızlı bir şekilde inceleme yapabilmekteyiz. Benim isteğim ise bütün yöntemleri eksiksiz veri setlerine, tek bir uygulamada, dinamik bir yapıda uygulamak.
Projenin Amacı ve Hedefi
 Aynı formatta seçilen veri seti üzerinde veri ön işleme tekniklerini uygulayarak veri seti hakkında seçilen niteliğin genel özellikleri; aykırı değer hesaplaması, frekans, kutu grafiğinin çıkartılması,  varyans ve standart sapması hesaplaması, var olan eksik verilerin silinmesi veya tamamlanması, veri  normalizasyonunu sağlayan dinamik yapıda bir uygulama yapımı amaçlanmaktadır.

 İşlemler:
 Nitelik özelliklerinin gerçeğe daha yakın değerlerde olması için eksik verilerin ortalama, mod veya medyana göre tamamlanması veya eksik verinin silinmesi.Bu iş paketi başarımın %15’ni kapsıyor. 
 Aykırı değerleri IQR değerlerine göre hesapladıktan sonra silinmesi. Aykırı değerlerin düzenlenmesi için normalizasyon işlemlerinin yapılması.  Belirlenen niteliğin ortalama, mod, medyan, maksimum ve minimum değerlerinin hesaplanması. Programın bu kısma kadar olan kodlama kısımlarının dinamik yapısının test  edilmesi. Bu iş paketi başarımın %20’sini kapsıyor.
Niteliğin beş sayı özetinin çıkartılması. Ardından birçok özelliği belirlenebilir olan sayısal verilere sahip niteliklerin frekans tablolarının çıkartılması. Bu iş paketi başarımın %20’sini kapsıyor.
Varyans ve Standart sapmanın hesaplamasını her niteliğin ayrı ayrı yapılması. Bu iş paketi başarımın %20’sini kapsıyor.
Aranan değerlere erişebilmek için arama fonksiyonunu yapılması. Programda ki eksikliklerin giderilmesi. Dosya seçim veya eksik veri tamamlamadan devam edilmesi durumunda oluşacak hataların engellenmesi.
Programın dinamik yapısının kontrol edilmesi ve teslim edilmesi. Bu iş paketi başarımın %20’sini kapsıyor.



English
Methods, Hardware, and Software Used in the Project:

On the Python programming language:

Pandas: A Python programming library created for data processing and analysis.
Numpy: A library that supports large, multi-dimensional arrays and matrices in Python and adds high-level mathematical functions to operate on these arrays.
PyQt5: A Python binding for the cross-platform GUI toolkit Qt, implemented as a Python plugin.
Tkinter: A library that allows visual programming with Python.
Os: A built-in Python module that makes it easy to perform operations on files and directories.
Sys: Allows you to get information about the Python version and perform various operations with the version you are using.
String: Provides additional tools for processing lists. Some methods available in the standard data structure are not present in the string module.
Pathlib: A standard Python module that provides an object-oriented API for working with files and directories.
Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.
CSV: The CSV (Comma-Separated Values) format is the most common import and export format for spreadsheets and databases. The CSV format was used for many years before attempts to standardize it in RFC 4180.
Math: This module provides access to the mathematical functions defined by the C standard.
Scipy: SciPy is a collection of mathematical algorithms and convenience functions built on the Numpy extension for Python.
Sklearn: Scikit-learn is probably the most useful library for machine learning in Python. The Sklearn library contains many efficient tools for machine learning and statistical modeling, including classification, regression, clustering, and dimensionality reduction.
Original Value
Interpreting the existing data in the dataset becomes difficult when there is a large amount of data, making manual inspection or calculation tedious. Data preprocessing methods allow us to inspect the dataset more efficiently. My request is to apply all these methods dynamically to the datasets in a single application.

Project Purpose and Objective
The aim is to create a dynamic application that applies data preprocessing techniques to a dataset in the same format and reveals the general characteristics of a selected attribute. This includes outlier detection, frequency analysis, box plot generation, variance, and standard deviation calculations, as well as handling missing values through either deletion or imputation, and ensuring data normalization.

Processes:

Handling Missing Values: Completing missing values based on mean, mode, or median, or deleting missing values to ensure the characteristics of the attribute are closer to real values. This task accounts for 15% of the project's success.

Outlier Detection and Normalization: Removing outliers after calculating IQR values and performing normalization processes to correct the outliers. Calculating the mean, mode, median, maximum, and minimum values of the specified attribute. Testing the dynamic structure of the code for this section. This task accounts for 20% of the project's success.

Five Number Summary: Generating the five-number summary of the attribute. Then, generating frequency tables for attributes with numerical data that can be used to identify multiple features. This task accounts for 20% of the project's success.

Variance and Standard Deviation Calculations: Calculating the variance and standard deviation for each attribute separately. This task accounts for 20% of the project's success.

Search Function and Error Handling: Implementing a search function to access desired values. Fixing program deficiencies and preventing errors when file selection or missing data completion is interrupted. Testing the dynamic structure of the program and final delivery. This task accounts for 20% of the project's success.
