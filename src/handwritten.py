from transformers import TrOCRProcessor, VisionEncoderDecoderModel

def model_installer(model_config_path):

    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

    processor.save_pretrained(model_config_path)
    model.save_pretrained(model_config_path)

class OCRExtractor:
    def __init__(self,pretrained_model_name_or_path):
        self.processor = TrOCRProcessor.from_pretrained(pretrained_model_name_or_path)
        self.model = VisionEncoderDecoderModel.from_pretrained(pretrained_model_name_or_path)

    def text_extract(self,img):

        pixel_values = self.processor(images=img,return_tensors='pt').pixel_values

        genrate_ids = self.model.generate(pixel_values)

        generate_text = self.processor.batch_decode(genrate_ids,skip_special_tokens=True)[0]

        return generate_text
