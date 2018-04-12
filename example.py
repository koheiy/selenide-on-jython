load("C:\\tools\\depend\\selenium-remote-driver-2.53.1.jar")
load("C:\\tools\\depend\\selenium-api-2.53.1.jar")
load("C:\\tools\\depend\\selenium-java-2.53.1.jar")
load("C:\\tools\\depend\\selenium-firefox-driver-2.53.1.jar")
load("C:\\tools\\depend\\selenium-support-2.53.1.jar")
load("C:\\tools\\depend\\guava-20.0.jar")
load("C:\\tools\\depend\\gson-2.7.jar")
load("C:\\tools\\depend\\httpcore-4.4.5.jar")
load("C:\\tools\\depend\\httpclient-4.5.2.jar")
load("C:\\tools\\depend\\commons-logging-1.1.1.jar")
load("C:\\tools\\depend\\selenide-4.2.jar")
load("C:\\tools\\groovy-2.4.12\\lib\\groovy-all-2.4.12")
load("C:\\tools\\depend\\groovy-2.4.12.jar")
load("C:\\tools\\depend\\ganymed-ssh2-build210.jar")

import com.codeborne.selenide.Selenide as Selenide
import org.openqa.selenium as Selenium

def getElement(self) :
    return Selenide.getElement(self)

Selenide.open("https://www.google.co.jp/imghp?hl=ja&tab=wi")
getElement(Selenium.By.id("lst-ib")).setValue("party parrot")
getElement(Selenium.By.name("btnG")).click()
