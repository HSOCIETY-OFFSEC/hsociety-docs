import pandas as pd
import os

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Compile the 30 organizations data
organizations = [
    # LAW FIRMS (6)
    {
        "Organization_Name": "Minkah-Premo, Osei-Bonsu, Bruce-Cathline & Partners",
        "Website_URL": "https://minkahpremo.com",
        "Sector": "Law",
        "What_They_Do": "Full-service law firm providing corporate, commercial, and litigation services",
        "Estimated_Staff_Size": "25-50",
        "Sensitive_Data_Handled": "Legal client records, corporate documents, confidential case files",
        "Contact_Name": "Managing Partner",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Ashong Benjamin & Associates",
        "Website_URL": "https://ashongbenjamin.com",
        "Sector": "Law",
        "What_They_Do": "Corporate law firm specializing in commercial litigation and advisory",
        "Estimated_Staff_Size": "20-40",
        "Sensitive_Data_Handled": "Client legal files, corporate contracts, confidential case information",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Renaissance Law Chambers",
        "Website_URL": "https://rlc.com.gh",
        "Sector": "Law",
        "What_They_Do": "Criminal defense and general litigation law firm in Osu Accra",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Criminal case files, client personal information, court documents",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Dotse@Law",
        "Website_URL": "https://dotselaw.com",
        "Sector": "Law",
        "What_They_Do": "Law firm specializing in criminal litigation and immigration advisory",
        "Estimated_Staff_Size": "20-30",
        "Sensitive_Data_Handled": "Immigration client records, criminal case files, personal identification data",
        "Contact_Name": "N/A",
        "Contact_Title": "Lead Attorney",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Sory@Law",
        "Website_URL": "https://sorylawgh.com",
        "Sector": "Law",
        "What_They_Do": "East Legon law firm focused on criminal litigation and immigration law",
        "Estimated_Staff_Size": "20-30",
        "Sensitive_Data_Handled": "Client immigration records, legal case files, personal identification",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Integri Solicitors & Advocates",
        "Website_URL": "https://integrisa.com",
        "Sector": "Law",
        "What_They_Do": "Law firm specializing in juvenile justice, cybercrime, and general defense",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Juvenile case records, cybercrime evidence, confidential legal files",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    
    # ACCOUNTING FIRMS (6)
    {
        "Organization_Name": "Prime Chartered Accountants",
        "Website_URL": "https://pca-gh.com",
        "Sector": "Accounting",
        "What_They_Do": "Indigenous Ghanaian firm providing accounting, tax, audit and advisory services",
        "Estimated_Staff_Size": "25-45",
        "Sensitive_Data_Handled": "Client financial records, tax returns, audit reports, business financial data",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "A.G. Neequaye Accounting Services",
        "Website_URL": "N/A",
        "Sector": "Accounting",
        "What_They_Do": "Accounting services firm in Asylum Down Accra",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Client accounting records, financial statements, tax documentation",
        "Contact_Name": "N/A",
        "Contact_Title": "Owner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "AA & K Chartered Accountants",
        "Website_URL": "N/A",
        "Sector": "Accounting",
        "What_They_Do": "Chartered accountants firm in Tesano Accra",
        "Estimated_Staff_Size": "20-40",
        "Sensitive_Data_Handled": "Client financial records, audit files, tax returns",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Adjei, Ansah & Associates",
        "Website_URL": "N/A",
        "Sector": "Accounting",
        "What_They_Do": "Chartered accountants in North Kaneshie Accra",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Client financial data, accounting records, business tax information",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Alex Thompson & Associates",
        "Website_URL": "N/A",
        "Sector": "Accounting",
        "What_They_Do": "Accounting firm on Atta Mills High Street Accra",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Client financial records, bookkeeping data, tax documentation",
        "Contact_Name": "N/A",
        "Contact_Title": "Owner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "AOB & Associates",
        "Website_URL": "N/A",
        "Sector": "Accounting",
        "What_They_Do": "Chartered accountants in East Legon Accra",
        "Estimated_Staff_Size": "20-35",
        "Sensitive_Data_Handled": "Client financial statements, audit records, tax returns",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Partner",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    
    # HEALTHCARE (6)
    {
        "Organization_Name": "Nyaho Medical Centre",
        "Website_URL": "https://nyahomedical.org",
        "Sector": "Healthcare",
        "What_They_Do": "Leading private medical center in Airport Residential Area Accra",
        "Estimated_Staff_Size": "80-120",
        "Sensitive_Data_Handled": "Patient medical records, health insurance data, personal health information",
        "Contact_Name": "N/A",
        "Contact_Title": "HR Manager",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Lister Hospital",
        "Website_URL": "https://listerhospital.com.gh",
        "Sector": "Healthcare",
        "What_They_Do": "24-hour private hospital in East Airport Accra",
        "Estimated_Staff_Size": "60-100",
        "Sensitive_Data_Handled": "Patient medical records, lab results, insurance claims, personal health data",
        "Contact_Name": "N/A",
        "Contact_Title": "Operations Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Akai House Clinic",
        "Website_URL": "https://akaihouseclinic.com",
        "Sector": "Healthcare",
        "What_They_Do": "Private clinic in Cantonments Accra",
        "Estimated_Staff_Size": "30-50",
        "Sensitive_Data_Handled": "Patient medical records, consultation notes, prescription data",
        "Contact_Name": "N/A",
        "Contact_Title": "Clinic Manager",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Franklyn Medical Centre",
        "Website_URL": "https://franklynmedical.com",
        "Sector": "Healthcare",
        "What_They_Do": "Medical center in Kokomlemle Accra",
        "Estimated_Staff_Size": "30-50",
        "Sensitive_Data_Handled": "Patient health records, medical histories, consultation data",
        "Contact_Name": "N/A",
        "Contact_Title": "Medical Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Ergon German Clinic",
        "Website_URL": "N/A",
        "Sector": "Healthcare",
        "What_They_Do": "German-specialty clinic in Abelenkpe Accra",
        "Estimated_Staff_Size": "25-45",
        "Sensitive_Data_Handled": "Patient medical records, specialist consultation notes, health data",
        "Contact_Name": "N/A",
        "Contact_Title": "Clinic Manager",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "OMNI Healthcare/Child and Associates",
        "Website_URL": "N/A",
        "Sector": "Healthcare",
        "What_They_Do": "Healthcare provider in Dzorwulu Accra",
        "Estimated_Staff_Size": "25-45",
        "Sensitive_Data_Handled": "Patient medical records, pediatric health data, insurance information",
        "Contact_Name": "N/A",
        "Contact_Title": "Medical Director",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    
    # NGOs (6)
    {
        "Organization_Name": "West Africa Civil Society Institute (WACSI)",
        "Website_URL": "https://wacsi.org",
        "Sector": "NGO",
        "What_They_Do": "Civil society organization in East Legon promoting governance and democracy",
        "Estimated_Staff_Size": "30-50",
        "Sensitive_Data_Handled": "Donor information, beneficiary data, grant documentation, program records",
        "Contact_Name": "N/A",
        "Contact_Title": "Operations Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "DAI Global Ghana",
        "Website_URL": "https://dai.com",
        "Sector": "NGO",
        "What_They_Do": "International development organization with Accra office",
        "Estimated_Staff_Size": "50-100",
        "Sensitive_Data_Handled": "Donor funds documentation, beneficiary data, project records, partner information",
        "Contact_Name": "N/A",
        "Contact_Title": "Country Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "DKT International Ghana",
        "Website_URL": "https://dktghana.org",
        "Sector": "NGO",
        "What_They_Do": "Reproductive health and family planning NGO in Kanda Accra",
        "Estimated_Staff_Size": "30-60",
        "Sensitive_Data_Handled": "Beneficiary health data, donor information, program participant records",
        "Contact_Name": "N/A",
        "Contact_Title": "Country Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "African Centre for Peace Building (AFCOPB)",
        "Website_URL": "N/A",
        "Sector": "NGO",
        "What_They_Do": "Peace building organization in Adenta Housing Accra",
        "Estimated_Staff_Size": "20-40",
        "Sensitive_Data_Handled": "Donor information, beneficiary data, program records, partner contacts",
        "Contact_Name": "N/A",
        "Contact_Title": "Executive Director",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Centre for the Development of People (CEDEP)",
        "Website_URL": "https://cedepghana.org",
        "Sector": "NGO",
        "What_They_Do": "Development NGO focusing on health, education and community development",
        "Estimated_Staff_Size": "30-55",
        "Sensitive_Data_Handled": "Donor records, beneficiary personal data, grant documentation",
        "Contact_Name": "N/A",
        "Contact_Title": "Executive Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Discovery Learning Alliance",
        "Website_URL": "https://discoverylearningalliance.org",
        "Sector": "NGO",
        "What_They_Do": "UK-registered education NGO operating in Ghana",
        "Estimated_Staff_Size": "25-45",
        "Sensitive_Data_Handled": "Student records, donor information, partner organization data",
        "Contact_Name": "N/A",
        "Contact_Title": "Country Director",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    
    # INSURANCE (6)
    {
        "Organization_Name": "Enterprise Life",
        "Website_URL": "https://enterpriselife.com.gh",
        "Sector": "Insurance",
        "What_They_Do": "Life insurance company in Ghana",
        "Estimated_Staff_Size": "50-80",
        "Sensitive_Data_Handled": "Policyholder personal data, financial records, health information, claims data",
        "Contact_Name": "N/A",
        "Contact_Title": "HR Manager",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "African Life",
        "Website_URL": "https://africanlife.com.gh",
        "Sector": "Insurance",
        "What_They_Do": "Life insurance provider in Ghana",
        "Estimated_Staff_Size": "50-80",
        "Sensitive_Data_Handled": "Customer policy data, financial information, health records, claims documentation",
        "Contact_Name": "N/A",
        "Contact_Title": "HR Manager",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "Allianz Life Ghana",
        "Website_URL": "https://allianz.com.gh",
        "Sector": "Insurance",
        "What_They_Do": "International life insurance company in Ghana",
        "Estimated_Staff_Size": "40-70",
        "Sensitive_Data_Handled": "Policyholder data, financial records, health information",
        "Contact_Name": "N/A",
        "Contact_Title": "Operations Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    },
    {
        "Organization_Name": "A-Plus Insurance Co.",
        "Website_URL": "N/A",
        "Sector": "Insurance",
        "What_They_Do": "General insurance company in Ghana",
        "Estimated_Staff_Size": "30-55",
        "Sensitive_Data_Handled": "Customer policy data, claims information, financial records",
        "Contact_Name": "N/A",
        "Contact_Title": "HR Manager",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Donewell Life Insurance Company",
        "Website_URL": "N/A",
        "Sector": "Insurance",
        "What_They_Do": "Life insurance provider in Ghana",
        "Estimated_Staff_Size": "30-50",
        "Sensitive_Data_Handled": "Policyholder personal data, financial information, health records",
        "Contact_Name": "N/A",
        "Contact_Title": "Managing Director",
        "Contact_Link": "N/A",
        "Priority": "MEDIUM"
    },
    {
        "Organization_Name": "Universal Insurance Company (UIC)",
        "Website_URL": "https://uic.com.gh",
        "Sector": "Insurance",
        "What_They_Do": "General insurance company, member of Ghana Insurers Association",
        "Estimated_Staff_Size": "40-65",
        "Sensitive_Data_Handled": "Customer policy data, claims records, financial information",
        "Contact_Name": "N/A",
        "Contact_Title": "Operations Director",
        "Contact_Link": "N/A",
        "Priority": "HIGH"
    }
]

# Create DataFrame
df = pd.DataFrame(organizations)

# Save to CSV
df.to_csv('output/accra_organizations_cybersecurity_training.csv', index=False)

print(f"CSV created successfully with {len(df)} organizations")
print("\nColumns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.head().to_string())
