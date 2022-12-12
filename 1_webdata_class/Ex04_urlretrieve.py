
# 크롬에서 구글이미지 > 오른마우스 > 이미지 주소 복사 >
# 구글 이미지 : https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
# 다음 이미지 : https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png

"""
    urllib 라이브러리(패키지):
        - URL를 다루는 모듈을 모아 놓은 패키지
        - Http나 Ftp를 사용하여 데이터를 다운로드 할 때 사용하는 라이브러리

        [예] request 모듈 : 웹 요청을 보내고 받는 기능을 하는 모듈
                - urlretrieve() 함수를 이용하여 이미지를 다운로드 받아 파일로 저장한다.
"""

from urllib import request as req

url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAADICAMAAAApx+PaAAACiFBMVEVHcEz7wmTmr3v623v923r823r823v52nxkkaxyq+b73Hn723r823un0s2ty/qtyvzvjWH82nv723n9z1T92nqsyvmsy/mtyvn9zVyuyvmp0NrvcGn2kIzzkovzkov3iIj93Hv0kYvykovykovykovykorxkYv703dBhvZBhPJChvNChfQ/hPVBg/L83HtBhPNBhPRChfNAh/RBhvRBhvRCg/RBhPRBhvPykotBhPRBg/RChfRBhfTykotBhfRBhPJKgVE2qlX72nqj2bNBhPVCgfQ9jPVLf1Azp1MzqFJNe1Kk2LKk2LKk2LJOeFFOd1FOd1FNd1FOeFFPeFJOeFBOeFFOeFFOeFFOd1FOeFE0qFM0p1NOd1JNd1FBhfRNd1FPeFJOd1GtyvqsyvtOd1GtyvqsyflAhfOtyvpOeFGi07K5uYlzl5SLmFVmhFdEc1VChfSku8eg1K5+rYdpnmNNdEVxnIAkqk6tyvY/fVRNemRMe3lza0v3ugVxhUNHgLrETzzpQjXvQDT5PTKj17Kk2LKk2LLpQTTrRTvFTjvpQjX7xgPutwr6ugT7wgP6ugVBhv3qQTTpQDPpQjTpQTTpQTPpQDLpQTSj17L6uwX/vAD5ugX5uAXpQTTpQTXoQDP6vgP6wAXqQzf6ugTpQTT7yAP6uwTpQzT6twX6vAVFfvToPzAfyfcZ0vguq/bsRz3wTkr1WVrqQzb5YWf3XWLyVFIptvYU3/gC/fkD/vYG+PoG/PkzofX/bXr/a3f/b337ygMD/vcG/Pg0f/z7uwNKdPM2nfUnuPZ2ndL6ZW3mOin82wL6sQX//wD96AH94gH//QD/7wD//wD//wD//gD//wDjv1P4tmouGKWkAAAA2HRSTlMAEAQyYFaZpgQKPp6THjdEClJJJmkrWVUbURQVPkgzJXNPWVOTo5mGHCc0Qk0TfVaBoLnQ2e734W+L5v/GgZX9FyBZLXbzwA211Jc9UVh9vrJS9OwrcNvORSD/xDuKr6b//HGJ46KbaZRhc3bFotv/Yq9hj8X/S/9k/////zr///////+Uo4Q6seJXuf/rxFT/LYOgZuv5c5v////3kOLyz9bMakmvjB//3///X0+MwKR711dnkno/FBsuKp03QC+gICX+ffyqnLpL/5P/N3GBT14+Q0hN2astPVRlAAAhZUlEQVR4AezBMQEAAAQAMNA/sxI+2wIAAAAAAAAAAAAAAAAAAAAAAM5kVvxCz3QFj9SyU1dJFQNRFEVv3EPcnru7u8x/UHRwh6Yanq7ob2rXCccLAs+ebnVREuEKj6woqqrwDJwmSdNvdI1UdoMxLRvOHyuoiOLAaXI93/d8F4gIHB5NwKSv0T9gGHAktNAPQ3RFQADtKLyq8rwM584S4g9VMD40kUyl0hSQFaRSGcDn+iHi+xoQYKu8iijZs5+6wQqIY/y8eS5fyOdTZKsni6VSOW8ALt2Pp+57JKLTDM+rCF8J4NwZsuPIBjyp1uoNpFmrteADdDJfQPJpIChdLhWL5VIBcGkewd/7Y/Q2BZejVet0e/3BcDSOTYaDfq/beZveyN1HTxlAzrRcRMpFAzCJuuf7vqeLQADVVuLmCgeXotacDebjxVvj+XLWqP5xdHqFosfwJybpaOmuBEQwqoJkqQvZeGc92Sw+sxnMmk9TotPkf+90vPSYAfik6JfJt7vtA/QGd+x9Nmvdcm8W/nHbUABWIZmvXbgYLAzCzMlvcVGbkzPjZsdyc5fGYyi3f/wsJxfZOuN15H0/KD7rrO+9J+liZzmv9TzqGQb/ByYf79IlTvPk6UKNbOQCyEYOdt5aIcsyZ2v6F3hNv1cuGBbNKZDEg6+/IXDFTqPD+wf1+kEPoIDVU764sVOAvXPtF8aDI1trbiAviBLoCEYSZIVTQy1jePe+WaLQWU2XjUID94+Pjo/EBzYtLP2bbwnfFcue/foBJl7rNic4VrUa++PVnaIczrSVA3QRQp5G5nO4cPezOA8F6CbATIzdHS9xPDYFhHEyuwxpTPcnAIHlFJOW/jW+F40F2fQchNRJqeMoBSEksKA6LOzulGBta5KKlxDGc+DZrDw7Ojq6UWiNlQx0SkMqUmM9PcMkJyAvo1M4Nq/Ox+7dvR94J7UuCUi2k6SzsqiCTB4d1EPpjyJlLqIQvjpl/tWTnXLszoAYGjrldLqGnzWbx83mDaZAmcuohdxKmay1tF6v79dImZ8j2CCTiXDbefd838nigZVE6VBHhlmu0iGvtLIPVISZ3Z3SPHkeM2qi83plAOhrngQcn/SAbKCmoyh5FcbgCgusX6TyBaP4ME86OWxA30AoXTpJwKw1vd5a06FEsk8DlYB5vrbTAXtfzUUvwqEzPFcFN7H0gN7UWbs1dIvMFaGRvZz21A9aGyhV0xGFaGct6UGZY+kTRFKG9ABDyus4Lee265HPwIIqUNva2+mMwylAgMR6g//+JFv6hSsDAw9/EMlckd8JPgNS2T84k27xOmpHcTI6xfi91ldJkthqEXKGdCS7dtbe4tGjGsCYnEJug6uG88mlNKfra9vbGxsb22tP0rJiZRIQGE0ms//jMW7vR2kb+Etdl3/6+Zdojbpk4oz0Pv0IV/r+wfdcRLnM+w3SKRyVST2x3b0bnDChL5DPmVLpresprs2ATKApEuXIkJhqOF9OXrFXDhcXpqdqmKmZX7cOV9eTdnNEOkaKqvjxt+Oj6ylVYv3wk/ILcd7QGAAd+dy6p2t2svdaUOq///HCQwTBBMA2IgO7Epve421ejwQrPEyTTq5mpRu3NcOLjFyRMgdzSc7Xdx/PztHJsbC1Shf8Mn1usyKL28uXyo+vLAbQMJbkCMQ4niu1dXQjyCJvs+3B8NUfLxovERlF55nWVpxgOJKVEBsMLHqI4OH2nSSd0ZTY1XwLAhqGtXlRRlT2VYLaYbvy7SViPMbUwvI67ZzGj5jzXr40RF6yVRaG0wRZ1ZZ40ZBRFPF8riw+vhs3RE2yLRZCHAst1fQ5QX/5EtH50p4yyGsNjDmNdQRDJtlCNg+0dOosiPF0wfFN1YKnhLfhGgqKYmgQVISt9ipfmq6l94XZ3YjzxNSwnMi2xsNilIYguI7juILRUGQUR4it37YYm+sw2BBELogV9IZMlCVstFi+gWKEsRgxiFWoWGSQYwIlPfEsiTyloQtieLmE22jwLKgKj/faVunZvC9rt+k6p7FdBSVDT7xsEOXkW/jEIA/RKK5JtXCVU9pH9BI/CFHeJp1kr559CwTdUUFlmH1Cb9+25kAe04e0cxrG5nSUjyJKELQBJVFB+Rhc0i5d5YwiAws+UZ4gnSw3Ra4mC5oFqsPkCuV8deFUWk6xL67TzmkYVRM8lIng2Kk5Q9cYjSz6VmJkICp3YMMxIQBZ0gmsL8ooE52TIKgQzBLd2qfx3+J3BoZBJr+u76Y7J5tbI61kFYO3WZCBJXF6ymx7QZ2qWfMMg4HTTMmBcTJwunQCDNJXSbtaYNwC1WKBdj6FZV2/GXC7J9soeWwqp95dQY9uvzxZMURXUxmQCzQdV4jv3U6DrQID2zweOJ4ruujyNhk4Xzq5DXw16pPogks6RnWYW0lwDnpuhg+V9tVyprVwO1FNX+MdIzwWa75plykNaEs4uIGnOQiWygQzahir44EFPhiZxJaTTt8GEjRNMulmU83T2srU2ctBtzGlXw/KgcPeVNAZIl47rc4HVmxAKC+duhryQWWZij8atT1DXhQJXhv4a6WzUljpvMWADrBwsGJ2EsuwAs42KrZj6dAt8LNTpjqF/isApNJLvjOQg+22lle9/CNklu/qKMDTXV4tOZ+s7xpeOK5IVvMc6a9f9F/oT1lrHEEOr+amX425/ubZm56KFPpS6y5qfTeCQr9xvYN87b91AVBQ32OTB+GKYhqIoDiwVLJFY2WOLSh99P7YxMWE7HPlyNVcFSTSd9JsNk96wX+TxfgBnezGh3uDbVwHzi8ODQ4MXGrXLnkohq6Wca6gGFzy50osTruBYriwmPSx4PHJCUDDCoiQ+vxjzxF+eKR5VPtvbt3jT74+BxGGO3pnYKira6Dr4RV69qGAKHiQTl6wZyal2+D8l/MDuQN7UsFKT3xpxyl0G73H4VNiR//NBr+wFzutzYGP5cJg10DAwyG6QmRE4RbvIrZcYKovdl3t7u6++pBqyZaCKLjC0u/fHaFTyKBTSGAqJ/0w6nz9V/DR3BoI6bqUK12Exbt7W7CT0GKuduOXDbsvJcS+PINkW4fSLbybfHsOQsiwQDvD/+X2PrlBFfo/KN2FJSr9F4oE6Vc++RRztYuWjmW/e/f+/ft37wL7ZaTfG6XaBmPp2PSHM7D/ROmg909m7qo7bTAA4/jTdJLU3eW6ek5d0tMMm0HncjUXzpm7b/BCAnWX1F0+5gidRHiRan7YDZo/EI8yIfcoH6aR7nr3d/NNt+bf3Y69+z9itSrNrUX6aazrX3XuIW4/r/3SeZlFjZ6t/8J893g8gvJBBcHj+f7t4724J+SMx1k4c+vHD6+X+PzKiXi93h+3z1EOiPGlOB2mYRMlSQrYoOjmVTqrcACKsq1W68lkBhrBXq9eXz/0GJurx8YZmw8M6g0Nj0AnN3wAgdS0XKhw1Q0eYVTB86O8ciN4dn/p1Xb3X/bqSNEryyqzoDM27iV+v89HfCFkN/xEkIHZ2QKSKIrSMw5AXRevchcHIik5JaWIgcbkFPEbTM8w0GB6ZFmW3jHQGhmanZud05qdXzBUz0lNPZWamqN+eE1DpxJabXS0taFat1DKHSH6eRhaBheXQp2JmhJ+aiIIkwuIYbITQHWn4d/9IDDQ6Z8mkSwHoeGUZFGUJSc0ilbmI1otgk5yXn2e+i+mqsHBRzDKt7lZWnT6YtjS8SlCMTVeClOTxTDJBaC2Vb0vYjUOSekaiWwcGs8kMUR6xkBtfZ5iHXqMeuEM+6aNpxE6WHuC0TfWSBS9YzCzZ2KYbANg51WaOBySfkKxlhVH9M15iq0Yu2LyRqrqHUIi0ZmZZRLV0gZMLF0ZtHJ4nM5qhstdFodkhjqktqHm2o3eA7Wk4XmKTQZ0VXf56DoTiZ61SGJZ6od5MekBWZKflRg2du/AYRknFFNBqHHPpJBnJVDLXZmPbGelCFTVTXxscUdnFkls0xswMc7ptHEwTLy/QVTV7jfxcFfvPTo417NnrhLDdByFMbpxU8+DiW78APRPY3KsZtAINYiqgY9PQwLRp/uhw7LQ2Y79S6fvo3Uw0ScJnXFsZXKa6K3ViKqbj08X9LJ6Cc0Eg1h+U3duv02jWQCfhK1EkVYK7UtEV0RaTRGloKEXN2woVOo2eRnmX+AVafYF7TsPldA0okpZoDFTNThNhtBcmuaeNElt1x7S2eZ+cf6f/T6nBR9fGofpSs1hOsQ0QjU/n/v5Tl6EtDQ9NK5lytR+1iU7sfAw/C3Q1xQxXCRCUm4v5Y3IY3jTkEEnpi4G+ryigL8G81v1TB2KnowNl2f0ndcJh62zxPxe1GrbnyXCg0KfiMmRu+OJZNzpT6UzMRJyfz9k43H2i4J+W6+iY/H3s4gwjoOyYdC8LcB8PpvLzVkP8vNzhWL0kAgPBv29AnmKZmIIOsvSTDoGqFNvLr9Pn/8/QLfiv0d/5Os/X9dfrG9ri+fI3P/sRpjYL3B8wUFwvHW2wBe5qCM8CPQ3FGQeS9E0SyPoMQvLMDSTIYG/Gi7z/vsdw5Urhj8PnZjum6QDccMKPBDDZ9f2ObK17VOx8HcXoJpH88VCseCwF3LELHpR4Lj90gDQ4TNLZmjEnEknY/5kikGqTrOZCPBXwwR9Kfzz2PLy9fELhm76QK72k3daJn48cB5xJNtbnk8GeRS3CJnnDgoFxPo4nMvZHRh6gT/YD+uGvuuGzFmaZuKUd5UkSS+VYTD1eGSIVB3m6b+/HEN98BHzhUKfeLeqQ/xv1E37jjpsKAHzOSdww9ZovoChc3+UcrnSMV8Ur/KHYZ3QYboZiWPmfjKTIRPifzGk7JY0OUSqfhVU5H7/7xiebbtykdAnnKt6hEy+0ZerbSllO7hu1q4nLOxh5j3o0VzpD3wlKv5cWB90kx/4c6zZTm9qIkPRJ97ERNobp9NO6PQ/DMVxVQB95MoFBXL6mWOB1AFzQLs/9al5qaIf8oUv0Pe+Qi9we3Z90D96peFHmmXodDlhOXHHaTZG0RNxMumNROCtXPYKzTOJT//P/PmaPjNwymZS2nb9qdu4Tw14UA1/MCDx68/BA5jjJNCjX6EX+eOwLuhvoXFnGDbjZixxb5pmkZpnkqsYOZTNy35IGfTT/zU2sjym6dNXFrVlXrU4815ZyIqseimKFF/IxGmEcfu6DPh2MOjZcvlCWx5PMChX9k/qxgtBLp5Czvc0/aAIVL0vdNM7maIzbMKbiJMJlj1JUPAuhqUsd4cAkdy1Ech8YIuBZe4sP19zy5G7nXHSf5J2JxNx5T8YHKj4JDPpQY+vclRdr9WDG41ASI7d9Vrt3HXYFu0pOs/lD1AgVygdHuQ5vvdHwKtrQt9NSj06TTMMjt39CTaFlFxVvLFN0zCF708N5m/8eR+rTNpN+JWVLJah/GzK7bQgPUlGzulRvfBA5MGdRrPWqm6068FKrd2qhKrwmfBNnD3GCxLoDl4kzPHR7KH1ocOxZDvORvleOM/v64H+hpTcQIZlsLDMCQreIuotlw8fLzXyC5yGHZU2tR5rVC+dKZalT5IUjXwhy9AskyEjWmZxYh0yd1U6baHT8uy0G8FKu9lpNwMeKfXtrTMDf1caxu1z2JofRB1ECZVjel/EbFS0+fk9PdA/Sm6ATGPo2K77verIY+93L/1grHzufWnlm2v4Sv+4SykqWQyDoJN0oowDIoQ9TUU0+qyvIfNQqyY0mwi6r1OpVmrNZrfTbriCwMC/OI08pIVlnK8VuSxRmstmCWs0ag1ns3OlUhZT53KEDuibUkuVYmmWTsc1XLn73atLrOQAlw10RUf/fDy4NK1W1CATLM1giXlPoWPqKSqiquqGDTnzbrPbFJohX7uCNb3b7Qq1hgtY+E+K0/ZhIpfHEVuptF8cjYYPDw4OS9FRPmsviQ9DYa4fdHgXEYqxnCRiGkrufzvQ9Pvwn2UDo3a22z1FTwLomVPmTIxkEuVT58gg6qrzRq89kHm7KXLu+nxCJdjA0JHUGsDCnzbXZwB0DgdspewBVzwO7/HIoh8XuINsaT7Ho284+kMHzSIqnUmqKzn5bhPHFEO6WWq232E2o8nYp2/zdFQ5ABtx0qfM6Vgk9RU6wyZUW1RHUnftqWM972JN94VaFY8IHV+2A0Hp+36TP8ThOUSWy5aO88VijrDmeC43b88Vi/nj0n6+UETPQX9Nl0L3utWRU2/XtO36MJxPf95338DYuPHcbH9FWZeJUCdnlBkInaadEWUxazwEKi8dAUOG0PF1p+uTUg8YVKAXC7NhlLflD0uHHAre9vFvXJTAjRf+UD90bfH6N7UqcAazwTQMmyiWcDlNW64tqxVqrz5VTtqBMI78ChlDz5xBx5LyKkO519KajKvVaX6B7modeRr4WpR2wyOz79Bd2XJcMTdv5fmDPbstyqPkPGez7x1w3KItJz4O+s27hlDvPmp68ivXl0euGYZj58x5QyyIOYJ+XXYn03blRzx8lOa3SQS7JyzrJJl0OWOhz6DTTmVf8hNU9B7hZrfd9oVQylbHkXwXiyDsSFR9+7VKIFfMLRIoZ7OWsoi5GNXZ9g74eeTU+cLiwz+p6f73b/r8Yy2PXU5dvwq3Sy39oP3WK3+5jkXWfb0KJk8fg9gdFDVolj5JJ8lEvBxLnbDsKfS0VNPFEy+GHamrrgs9wG2h1XCFGoFgoNWstU9VvRKUx+8rEug4ZeP3S45DeynLFTF07OLtx47SIY+1Xgd07QkQt/PVecGb8VpvIYd5GLK2h9Y7/aDLbuSZSl/V6JSmaykRMEujfKe8ulour0bKbmdajOdx5i536mapS/c1BazlnWZlx1PdClbxV2i93haw8rfrHgn1gFHWbwlncby2TxBze9xZDZ7bWySIQxzhRRcGK87AXnC/DM00BhTkUlfl4MexQDGaR0aU5v2OWqZv8kut+wmN6aZiZdLvJ91xJ+mN+ctl56nRj0dkpdgXLomiB7oi87qv6trxBUNHG1uuDV/VcyQIOJRrSUK57R0T/nGWJNCPOR7VW3O5wilzTB1ZfGzbkc7rqcitkerldRi8qWv6pYaOxiOBzGpSv7I8gmZrxtXSNRj9T1CKPkWKKsfSbDoSt9B+pPuJZDkmUmcTERDJwSw9WMEuvVN3VdfrNbEa5woJqBpXDQiifV8PgkgO3kxY7KwWOYReIkUOPwJ80TFow2Ww8rqoIcvXLm3F5vlDvdTHr41dM4OMDx4TnLvXe98uBbvQSPzlOM2y8UgC/a+cQB2XGC7MQei9ufHfpMF7o4OYN0PVitDubHhQaW4dRXLtFvoD9I1m7Sgoq8SOgtbqPi64qgofJXS1Vp3y4G1T55Cz0YzS2yum4fnQHseU5q0YjSAemIVRIFZ0+bxJJGNBip7Ao0Y0Q1Epmk2X/TSuwXqxs6fTXthfBdA99Q5y3ZUqStaRAw81OwJ63e7i1y0Bf0cOHYcYsDyjKkVu4CEKLE5dSi4/LD8EaRuWeTDRqvto6OyoGvQEKxZl0jRjySB1Z2gmiRtWLLpgRbuvDX0bQ0c1d1cLQQ9UK+2u0MIXzU4A1eBVod+xwT6blqLb9I5L6RyKeQUswFB+hgtxf1RHi86mNRIJNZ1FZN1JXGp3u9M0tuhlP1L7E7efxppOna/pKEavbpwpOorp8CiFINRxAq8G/SowW0RUlXqx6NA9GKnvhOJHktocNuorD+Xi6KfsUzM4UFY/4L4mM+90yuunLUyyV4uj6RjSeAudROi1zDuAjjDXkBtv1JrYwfuqFXS5vd4RVKH/sADH3jkV5vl93SPQ77WGuoC8SeK2y5Aou+lveFea6tij7fHU1XNC/hWo5rBbIw/kaMYfSaT9ZSd9lpyXY6gc62T7BXLBBjLlLZer3ghVj9q9igwK5QMt0dY3awEIXflBFWFHIa9gfpAd9LADeCqVstuzB9TmMHRezA8mJycfmUEYLsU+fU/Dma9Aby6fu4GjZaI+U+WyN95jjqnHyHLZn0KX4FSQV5myodQMp2hV11FHEJttzVp9p1qtbrSEpiBsSKDvGNSSkfBcThbCc/lsKfzNx5reGlX0/IsPGAJlNz2YvPX995MPTFh1F9UOLsyuTCvUferZjFXlCbkr/Yv98h4bncpk0vTXkjuTyGROxEvnqrw4I63IbTRx1b1+VKlj5qdF+G7jqNEUZ2lCEugbJpXhLTwemeX5oiRuzx2X9B9gVKbqHxTV102JXUtees9uuYWYf3/rlkVkqUIdc1+cWZm+fe/eKPp1b2r62eNZ65La2yTMYRl2tTdbRuODvV+FPr2mTyhFGdYnHYPCmVm3026fMcfUhQ66FNtskjn44NGZDk4TkHrYsZfDJRqe5/hibt86+FFlIElgxI1rThKYAufuUECfvNlz05r7mBbsxByabp8jFhY03mF/Jj+qCp26ptAJMFlowmYiIG24VFDEriGyMYrPoF0MsC/NH2b3otG9veyxbfClBE5le21t14Rld23TSQ7Z5hnDo0kEffKRAW5eG1yIHxQZjMy+a0pMeQ7ss7Qk5+sKGtSb7ZZ0ONLzAtYJoSyFF2xWIvxt60colY6LE4tfZbncpbfvN2+hQO7W3750SVfs38TcCmy7whFGMprQ4bwU+VE59C5OyqhLLVCVvHHH3H+51NLgi4a0t5yS6JdSPlz++UjLg0cPLNIqzZx+1PBTOs9ZPxHxpjSo41RO6i0nlMOwQV9T3cCjKB5MRn4G6YX1IrdLGd+v6pV3QzEuJ5t0vD2zMCDypZnbqhUqKXVchVGKJF+DSfDnLYlUAzWlgVeOyMm2Dk1bLww6lrfDzrzPJ8g9H0zZ55/BnE51JVMkTtOqxt2rumpq3AWoV1SoNzudjar0XesGeV/g4taEYuqkLuYT3w2p3L5v0418YWZKsp//x1FJ/E5C6gx9LnO4VO7TFhiCrnQU1DtNELlDRVdPRqA87r8QGMgrd1/k5FvTd8MrU/8g9CGf/VK6Mf6EPi/i5c83tNZ9k84TmbKzdMYb0ch1xkPw+GKg2Ubp+il49JvQaYm1OFiZGf3rDamvGr1PaPukx4Os/jaOog8rW/P3YZ4Uw9Chxt7fyBNP73617E9+/RUvcP639r7vZIJmv3BHL9POiDLuNZpv3rSYgFdHgtbANoRORxB6M7CddrOCS3FQ0a/+88mTJz/eACb+6YKGaUeU7+uGPvrTLy9/efKd6S11DnI3Xpc07HL7+QwsvUGxL96fBvubMfOXv/5y4zutPRQRMpbAhTgsNJN2ujFzWTXOePPvSFALyLyxBbF7NhrIjXfa6EtoVXyyjRT/Y+8Mftq4gjA+fonxronjrS23xgs4mAOwNhjC2hEIOaqN00pr33qL5APImyi50Jy4cKsCokpQgQQrBZESAkU50Kb0bgkOUTn0Rv+dvh2XxbvetdeYFNnyz1w4oeHzvJ197818b/YIpLIZBRbKYKK5tNEzSQCt6HOAfFcu+kM1tmfUcKJQyDKwuGUm+/bSLrQEzFB0bDxmtDaKd0d1bvns85LoP7iM3tVV2T8u/Xl09MfR77/taCRHlgEgGKJWaGiMhbcjtVMJDl4WT/8+PS2+1c8kwHf0QAZFz6ZAw3A4IWq/u/fGwgzoRI8A8vW3Dy9QLfukQgFDS6Fxz85rg4V9a5GDloEZFuYmclNiLB2npGNpcSqXGI0MsqABJ7VrMh1ZxjpNP0lXwaApbAsovVR0SogH8q5ytMzPv27SDwV/1fUpuzJIVqqMITKaG8cI0pMPxh4NMZVu0lEo8U0ZaoxZGhrlP2sZfnfrcPtC+NfbO2vr+wRaDnZQEMLRaDQsCEPDYEyqgH4RmdrDIj/Qj9mglm5VdCBYwVsCe1sCxqIjDNAIItGI4DLu142HwQyd6Aj30/L66prC1sbyIq/9S80FYdkG7N8Z6Tmt3jNEP+jdIks8qJneF+rDRpeiVc1PgMJKWVTdVS0Gr1O9zMs8sNTggT52Bd2TCyH4o8HVNd/lgyYiIGWkFGnEJUSSXKCDrL6uR3Ow9Siqo4G1ZdVfvAPElclmstkUmMPd7HQ4BryVt/2xAc+cTEFBguqg1aacf+xmoDnAfxlFMlGdvWwgZH3bwsDIi40svruvrycIJcjepgXN1V2ZQEqSXKTKCuVxdN7qcIzYKg7dcyxURXry/EkKTNF5prugSSBSqfZ1gQGBrpkZNwuXYxdreMtjoAnPc6CyclBL85cLYIYwOq1RnbvjQNdlZ8VV0DEGamAlence7bPz7uZJdORZytgWWpbl+cuqvl9jDvThYhX7Rm9xs2qan9jMVAon7unsBbmRTjTg9ah3qhoasEQIaOmiolPkriZa3c1qX2YGg8lfPpbdwyp7lxs8VIOs/Gg6GHazaJbmg4+mYpUpfNNxYcAbiTdmPWm7Ud7ghdzOy5jpt6FJYDKmy3vgMSI3YADPrS9tG3f8buxDLbiV95vUXreiZn9RXCAmST6h7sdEoQz/gINWcvpExw68evF7kvZk8oY+O2Sq+UwAmoVUlvJMIlcvOkJ2V3dKW5gfkL/okNiPa8v7YAWycPLLizfIeY4fvH+3AGAoupCLmXmL+O3nBryP9IMUEM5q9xlxJg069QMzsiyj5s1CSspkJNbwkS6j6DMMNAS/uLG2tPNqW+HV4drq7j5YhTDz3zvOzs4OKG9fvi/urXjN1QnHNX20QsWVEX3DWzwCCNfb198TBCvYaJe+wchsxuf2sU22OUPAELcsK4nug8bh9gf+QTxQF67Zx7Ozs3L+qdfr5831VucemauOCKKmgQt1wsMeSrAO0e1OAi0K0zVLuZryxDZyS6HjDgFzzFcbNxCoiZDWHrBEGdDAzk0a3ZXilbMePOypDecpZboXWpeAzxeAeuCDwSAHBvgHOvC1aYSDuvhKqYzzsg+skDjWXeITmPIyL3ffwJQAT/gooR4OakO89qTdjrOjWhYG6iPYr5yK84aZju/KjpsE6gBrpLzFHU6/M3nvWH/dY1oYZFmWduiM4r0Ko0EKPO77WxMdxyh+UTYlro2tP2SaM87Ozo4Oxy0/1Anrnv/SBZZW3qTz6TGqXs6kOHV3ShTVwr5yC5YoR3xWnulqpU8AaaM9FTfASZ/qd7yfb7nx2mkKFlB0K0wKcI6tOxTq772Ukm3UU3G/ychULwefjxvKG7TnkzXVcXFXIf4gD5ehDZZECA/XgBdF93yypvk0XA1tuNKp+PWslDZPUhlw6Bz7fzVvY+umdXAvB9cAbosn7U6Oma7ZnxW/Ss3bXOvTkZpDY9UQFWs0ZEWhTcsxlEibS55ODEGbFoQJm7W4xHNhBtq0quwJsUL3uDjR2pK3GYompsYnY/H7lNikOH53IjIIbVqewfDo2ANxXBzPJeaEYfi3PTgkAAAAABD0/7UnjABwAAAAAAAAAAAAAAAAAAAAAAAAAAAC4bKs2t6g/gIAAAAASUVORK5CYII='

req.urlretrieve(url,'data/myimg.png')

