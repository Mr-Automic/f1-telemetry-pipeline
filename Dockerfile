# 1. الصورة الأساسية (بيئة بايثون خفيفة)
FROM python:3.12-slim

# 2. تحديد مجلد العمل داخل الكبسولة
WORKDIR /app

# 3. نسخ ملف المتطلبات أولاً
COPY requirements.txt .

# 4. تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# 5. نسخ كافة الأكواد إلى داخل الكبسولة
COPY . .

# 6. التنويه عن المنفذ المستخدم
EXPOSE 8000

# 7. أمر تشغيل السيرفر
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]