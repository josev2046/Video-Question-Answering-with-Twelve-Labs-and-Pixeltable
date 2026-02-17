import pixeltable as pxt
from FINAL_my_functions import analyze_compliance, get_summary, get_decision

PROJECT_NAME = "twelve_labs_compliance_demo"

def main():
    print(f"🚀 Initializing Twelve Labs + Pixeltable Governance Platform...")
    
    pxt.drop_dir(PROJECT_NAME, force=True)
    pxt.create_dir(PROJECT_NAME)
    
    # Define Audit Log
    compliance_table = pxt.create_table(f'{PROJECT_NAME}.audit_log', {
        'video_url': pxt.String,
        'creator': pxt.String
    })
    
    # Register Multimodal Intelligence
    compliance_table.add_computed_column(report=analyze_compliance(compliance_table.video_url))
    compliance_table.add_computed_column(summary=get_summary(compliance_table.report))
    compliance_table.add_computed_column(status=get_decision(compliance_table.report))
    
    # Test Submissions
    test_submissions = [
        {'video_url': 'https://www.youtube.com/watch?v=icD8IxqxBD4', 'creator': '@RaeMorris_Pro'},
        {'video_url': 'https://www.youtube.com/watch?v=4PNRGaD_NhQ', 'creator': '@SmithaDeepak'},
        {'video_url': 'https://www.youtube.com/watch?v=RvQpoT9iD54', 'creator': '@SpainOnAFork'},
        {'video_url': 'https://www.youtube.com/watch?v=mdL-GkCmvb4', 'creator': '@RicardoGorski'},
        {'video_url': 'https://www.youtube.com/watch?v=Oz01bOgkQ7Y', 'creator': '@DoctorEyeHealth'}
    ]
    
    print(f"📥 Auditing {len(test_submissions)} videos via Twelve Labs API...")
    compliance_table.insert(test_submissions)
    
    # Print Final Presentation Report
    print("\n" + "="*90)
    print(f"{'CREATOR':<17} | {'DECISION':<10} | {'TWELVE LABS INTELLIGENCE / SUMMARY'}")
    print("-" * 90)
    
    results = compliance_table.select(
        compliance_table.creator,
        compliance_table.status,
        compliance_table.summary,
        compliance_table.report
    ).collect()
    
    for row in results:
        icon = "✅" if row['status'] == "APPROVE" else "❌" if row['status'] == "BLOCK" else "⚠️"
        engine = row['report'].get('tl_engine', 'Multimodal')
        
        print(f"{row['creator']:<17} | {icon} {row['status']:<8} | 🤖 {engine}")
        print(f"{'':<17} | {'':<10} | 📝 {row['summary']}")
        
        if row['status'] != "APPROVE":
            violations = [f"{k}: {v}" for k, v in row['report']['policy_checks'].items() if "Clean" not in str(v) and "Pass" not in str(v)]
            print(f"{'':<17} | {'':<10} | 🚩 EVIDENCE: {', '.join(violations)}")
        print("-" * 90)

if __name__ == "__main__":
    main()
