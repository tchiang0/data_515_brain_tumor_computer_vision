## Functional Specification

### Background
As the field of deep learning continues to grow, we are interested in its application within healthcare, particularly in the realm of brain tumor detection and classification based on brain CT scans. Our project objective is to develop a user-friendly website catering to a diverse audience, including researchers, patients, doctors, and interested users in general. The platform's primary functionality involves allowing users to upload brain CT scans and receive predictions regarding the presence of a tumor and its severity. Other features of this website includes a background introduction of brain tumors, its symptoms and signs, and resources to further explore the topics.
As a stretch goal, we envision incorporating an interactive chatbot into the website. This chatbot would serve as a guide, directing users to relevant pages and, ideally, facilitating the upload of images for predictions within the chat interface. This feature not only enhances user engagement but also provides an intuitive and seamless experience for individuals seeking information or diagnostic insights.

### User Profile
Potential users include neurologists, patients, and researchers, each of whom can actively engage with the website. This involvement may include navigating through various resources, uploading brain images for patient diagnosis, and interacting with the chatbot through typed prompts (stretch goal). Researchers, in particular, have the opportunity to deepen their exploration by reviewing the code, comprehending the model architectures, and gaining insights into how brain tumors are predicted to be their respective severity categories.

### Data Sources
We have two distinct data sources from Roboflow, catering to either [semantic segmentation](https://universe.roboflow.com/tumor-azexj/tumor-vliim/dataset/4) or [instance segmentation](https://universe.roboflow.com/mycollege/tumor-detection-2/dataset/3). Both datasets comprise brain CT images, depicting scans with and without brain tumors. Semantic segmentation is a deep learning algorithm that assigns a label to each pixel in an image, essentially allowing both object detection and classification. The dataset includes three classes: tumor_good_chance, tumor_moderate_chance, and tumor_less_chance, indicating the severity levels of detected brain tumors. Notably, a single image may contain multiple tumors, all standardized to a size of 640 * 640 pixels. The training set comprises 1187 images, the validation set includes 337 images, and the test set comprises 177 images. Each tumor class is appropriately distributed across these sets. For instance, in the training set, there are 516 instances of tumor_good_chance, 429 of tumor_moderate_chance, 244 of tumor_less_chance, and 7 brain CT images without tumors. It's important to highlight the presence of class imbalance, with observations ranging from most to least frequent: tumor_good_chance, tumor_moderate_chance, and tumor_less_chance.
On the other hand, instance segmentation utilizes a deep learning technique for identifying and distinguishing objects within images, essentially encompassing object detection. This dataset includes 3590 images, with 3140 in the training set, 300 in the validation set, and 150 in the test set. These images depict brain CT scans with or without tumors, with brain tumors in  most images.

### Use Cases
Some potential users are neurologists, patients, and researchers. Neurologists can utilize the tool to obtain a second opinion on brain CT images of their patients, provided there is written consent. This process not only offers an additional perspective on the diagnosis but also serves as a catalyst for introducing patients to supplementary resources. The tool's predictive capabilities enable neurologists to compare the model's insights with their own diagnosis. If there is alignment, it reinforces their confidence in the assessment. Conversely, in cases of disagreement, the tool prompts neurologists to investigate further into the patient's condition, facilitating a more thorough examination and, ultimately, a more assured diagnosis. 
Furthermore, patients can turn to this website as a valuable resource to enhance their understanding of specific medical conditions. By providing links to resources such as the National Brain Tumor Society and Seattle Children’s Hospital, the platform serves as a gateway to additional information, aiding patients in delving deeper into their diagnoses. The inclusion of an interactive chatbot (a stretch goal) adds another layer of assistance, allowing patients to navigate the website and access relevant information in a manner that suits their preferences.
Brain-related researchers can also engage with our website and, potentially, delve into the backend code to gain insights into how computer vision techniques, specifically instance segmentation and semantic segmentation, contribute to advancements in early-stage diagnosis of brain tumors.
