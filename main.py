import json
from lxml import etree
from selenium import webdriver


class TestA:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_a(self):
        res = []
        domain = "https://www.google.com/"
        self.driver.get(domain + "search?q=%E7%96%AF%E7%8B%82%E6%98%9F%E6%9C%9F%E5%9B%9B&sxsrf"
                                 "=ALiCzsYBRrQMbO67DT6NidzQ7b2vSG00uQ:1665828922748&source=lnms&tbm=nws&sa=X&ved"
                                 "=2ahUKEwjPo8mpgOL6AhVJEnAKHTI-CXwQ_AUoAnoECAIQBA&biw=1707&bih=924&dpr=1.5")
        page_source = self.driver.page_source
        html = etree.HTML(page_source)
        pages = html.xpath('//a[@class="fl"]/@href')
        pages.insert(0, "search?q=%E7%96%AF%E7%8B%82%E6%98%9F%E6%9C%9F%E5%9B%9B&sxsrf"
                     "=ALiCzsYBRrQMbO67DT6NidzQ7b2vSG00uQ:1665828922748&source=lnms&tbm=nws&sa=X&ved"
                     "=2ahUKEwjPo8mpgOL6AhVJEnAKHTI-CXwQ_AUoAnoECAIQBA&biw=1707&bih=924&dpr=1.5")
        for page in pages:
            self.driver.get(domain + page)
            page_source = self.driver.page_source
            html = etree.HTML(page_source)
            search_results = html.xpath('//a[@class="WlydOe"]/@href')
            for result in search_results:
                self.driver.get(result)
                page_source = self.driver.page_source
                html = etree.HTML(page_source)
                ps = html.xpath('//p/text()')
                sections = html.xpath('//section/text()')
                sentence = ps + sections
                news = {"URL": result, "sentence": sentence}
                res.append(news)
            break
        return res


if __name__ == "__main__":
    a = TestA()
    a.setup_method()
    List = a.test_a()
    json_list = json.dumps(List, indent=1, ensure_ascii=False)
    fo = open('sample_output.json', 'w', encoding="utf-8")
    fo.write(json_list)
    a.teardown_method()
