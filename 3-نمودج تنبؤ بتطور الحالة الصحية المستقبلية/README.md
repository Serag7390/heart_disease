# نمودج تنبؤ بتطور الحالة الصحية 
في هدا المشروع تم دراسة بيانات لمرضى القلب وتحليل بياناتهم وتنظيفها وانشاء نمودج  بعد تجربة عدة نمادج واختيار النمودج صاحب اعلى نسبة للصحة ثم تم بناء نمودج تنبؤ بالتطور المستقبلي  وتم انشاء واجهة رسومية لتسهيل التعامل مع النمودج  




# طريقة التشغيل 

انشاء بيئة افتراضية(.venv) وتفعيلها 

py -3 -m venv .venv 

.venv\Scripts\activate

تتبيث الملف requirements.txt المرفق مع كل نمودج 

pip install -r requirements.txt

فتح الملف

 python model_api.py 

سيظهر رابط في cmd انسخه و ادهب الى المتصفح الخاص بك والصقه سيتم فتح الواجهة الرسومية لكل نمودج 



او للتعامل مع api مباشرة  يمكنك استخدام :





{
   "age": 56,
   "sex": "Male",
   "dataset": "Cleveland",
   "cp": "asymptomatic",
   "trestbps": 130,
   "chol": 236,
   "fbs": true,
   "restecg": "normal",
   "thalch": 155,
   "exang": true,
   "oldpeak": 1.4,
   "slope": "flat",
   "ca": 1,
   "thal": "fixed defect"
}

مع تغيير المدخلات 


