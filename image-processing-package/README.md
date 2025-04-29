# Projeto: Pacote de Processamento de Imagens

### Descrição

O pacote "image_processing-test" é usado para:

- Módulo `processing`:
  - Redimensionar imagens;
  - Calcular similaridade estrutural;
  - Fazer correspondência de histograma;

- Módulo `utils`:
  - Ler imagens;
  - Salvar imagens;
  - Exibir imagens com `matplotlib`;
  - Plotar histogramas;

---

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar image_processing_tools.

```bash
pip install image-processing-tools
```

##   Uso 
```python
from image_processing_tools.processing import resize
from image_processing_tools.utils import load_image, plot_image

img = load_image("caminho/para/imagem.jpg")
img_resized = resize(img, 200, 200)
plot_image(img_resized)
```

## Author
Gustavo Luiz Gordoni

## License
[MIT](https://choosealicense.com/licenses/mit/)