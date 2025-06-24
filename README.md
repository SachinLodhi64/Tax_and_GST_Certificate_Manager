This code defines a desktop GUI application using Python's tkinter library for managing and organizing Income Tax Return (ITR) and Goods and Services Tax (GST) details along with uploading and downloading related documents. It offers a simple digital document management and data entry solution for small tax consultancy businesses or individuals managing client tax records.
 What the Code Is Doing
✅ **1. Authentication System**
Displays a Login Page with hardcoded credentials:

Name: 

Password: 

On successful login, user is taken to the main menu.
<img src="https://github.com/SachinLodhi64/[Screenshot 2025-06-24 174157](https://github.com/user-attachments/assets/c1f6e2b9-3341-4160-926f-cb43b334eb00) width="800" height= "500">

✅ **2. Main Menu Options**
Users can choose from four options:

Fill ITR Form: Enter and save ITR-related client details and upload PDF files (ITR and Computation).

Fill GST Form: Enter and save GST-related firm details and upload GST certificate.

Download ITR and Computation: Retrieve and download previously uploaded ITR files using PAN and assessment year.

Download GST Certificate: Retrieve and download GST certificate using GST number.

3. Form Functionality
🧾 ITR Form:
Inputs include:

Client name, PAN, DOB, Contact, Father’s Name, Address, Assessment Year

Uploads:

ITR PDF

Computation PDF

Saves data into ITR_Data.xlsx file.

Files are stored in local folders: uploads/ITR.

🧾 GST Form:
Inputs include:

Firm name, Active GST, Proprietor, Inactive GST, Address

Uploads:

GST Certificate PDF

Saves data into GST_Data.xlsx file.

Files are stored in local folders: uploads/GST.

✅ **4. Download & Print Options**
Files (ITR, Computation, GST Certificate) can be:

Downloaded via asksaveasfilename

Printed using system's print command (os.startfile(path, "print"))

**🎯 Problem It Solves**

This application helps in:

🗃️ Digitally organizing client tax records in a structured Excel format.

📂 Storing & retrieving tax-related PDFs (like ITR forms, computation files, GST certificates).

🧑‍💻 Reducing manual paperwork and Excel errors by providing a guided data-entry GUI.

🔎 Quick search & retrieval using PAN/GST numbers and assessment years.

**Who Can Use This**
This application is ideal for a wide range of users involved in tax filing and record management. Tax consultants can use it to efficiently manage and organize client ITR and GST records, streamlining their daily workflow. Accountants will find it useful for maintaining structured PDF documents and Excel logs of client filings without manual duplication. Small CA firms can adopt this tool to offer digital record-keeping services without the need to invest in custom software development. Freelance tax filers can securely store and retrieve client data directly on their local machines, ensuring quick access and reliability. Additionally, the user-friendly interface makes it particularly beneficial for non-tech-savvy individuals who need a simple, GUI-based solution without the complexities of web or mobile app development.

