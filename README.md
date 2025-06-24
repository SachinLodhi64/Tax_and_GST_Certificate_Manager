**This code defines a desktop GUI application using Python's tkinter library for managing and organizing Income Tax Return (ITR) and Goods and Services Tax (GST) details along with uploading and downloading related documents. It offers a simple digital document management and data entry solution for small tax consultancy businesses or individuals managing client tax records.**

**Problem:** Requirement of forms where the user can enter the data relevant to Tax filing i.e. Clients' details, its' ITR and Computation according to that assessment year. Along a form is required to enter the details of GST clients and their active certificates. The files which are uploaded should be store at common place in excel files, so that in future as per requirement the user can download or print the files. (Note: The forms should not be made separately)

 **Process of code run along with the screenshots**
 
✅ **1. Authentication System**
Displays a Login Page with hardcoded credentials:

Name: 
Password: 

On successful login, user is taken to the main menu.
<img src= https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174157.png width="800" height= "500">

✅ **2. Main Menu Options**
Users can choose from four options:

Fill ITR Form: Enter and save ITR-related client details and upload PDF files (ITR and Computation).

Fill GST Form: Enter and save GST-related firm details and upload GST certificate.

Download ITR and Computation: Retrieve and download previously uploaded ITR files using PAN and assessment year.

Download GST Certificate: Retrieve and download GST certificate using GST number.
<img src= https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174223.png width="800" height= "500">

3. Form Functionality
🧾 ITR Form:
Inputs include:

Client name, PAN, DOB, Contact, Father’s Name, Address, Assessment Year

Uploads:

ITR PDF

Computation PDF

Saves data into ITR_Data.xlsx file.

Files are stored in local folders: uploads/ITR.
<img src= https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174244.png width="800" height= "500">

🧾 GST Form:
Inputs include:

Firm name, Active GST, Proprietor, Inactive GST, Address

Uploads:

GST Certificate PDF

Saves data into GST_Data.xlsx file.

Files are stored in local folders: uploads/GST.
<img src= https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174302.png width="800" height= "500">

✅ **4. Download & Print Options**
Files (ITR, Computation, GST Certificate) can be:

Downloaded via asksaveasfilename

Printed using system's print command (os.startfile(path, "print"))
<img src= https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174318.png width="800" height= "500">
<img src = https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174332.png width="800" height= "500">

**Below are the data stored in excel files which is entered by the user.**
<img src = https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174437.png width="800" height= "500">
<img src = https://github.com/SachinLodhi64/Tax_and_GST_Certificate_Manager/blob/main/Screenshot%202025-06-24%20174518.png width="800" height= "500">

**🎯 Problem It Solves**

This application helps in:

Digitally organizing client tax records in a structured Excel format.
Storing & retrieving tax-related PDFs (like ITR forms, computation files, GST certificates).
Reducing manual paperwork and Excel errors by providing a guided data-entry GUI.
Quick search & retrieval using PAN/GST numbers and assessment years.

**Who Can Use This**
This application is ideal for a wide range of users involved in tax filing and record management. Tax consultants can use it to efficiently manage and organize client ITR and GST records, streamlining their daily workflow. Accountants will find it useful for maintaining structured PDF documents and Excel logs of client filings without manual duplication. Small CA firms can adopt this tool to offer digital record-keeping services without the need to invest in custom software development. Freelance tax filers can securely store and retrieve client data directly on their local machines, ensuring quick access and reliability. Additionally, the user-friendly interface makes it particularly beneficial for non-tech-savvy individuals who need a simple, GUI-based solution without the complexities of web or mobile app development.

