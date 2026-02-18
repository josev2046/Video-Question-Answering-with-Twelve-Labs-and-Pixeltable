import pixeltable as pxt
from FINAL_my_functions import analyze_compliance_live, get_summary, get_decision

PROJECT_NAME = "twelve_labs_cloud_governance"

def main():
    print(f"🚀 Initialising Cloud-Native Twelve Labs Pipeline...")

    pxt.drop_dir(PROJECT_NAME, force=True)
    pxt.create_dir(PROJECT_NAME)

    compliance_table = pxt.create_table(f'{PROJECT_NAME}.audit_log', {
        'video_url': pxt.String,
        'creator': pxt.String
    })

    compliance_table.add_computed_column(report=analyze_compliance_live(compliance_table.video_url))
    compliance_table.add_computed_column(summary=get_summary(compliance_table.report))
    compliance_table.add_computed_column(status=get_decision(compliance_table.report))

    test_submissions = [
        {'video_url': 'https://github.com/josev2046/Video-Question-Answering-with-Twelve-Labs-and-Pixeltable/raw/main/MECCA_Beauty.mp4', 'creator': '@RaeMorris_Pro'},
        {'video_url': 'https://github.com/josev2046/Video-Question-Answering-with-Twelve-Labs-and-Pixeltable/raw/main/Smitha_Deepak.mp4', 'creator': '@SmithaDeepak'},
        {'video_url': 'https://github.com/josev2046/Video-Question-Answering-with-Twelve-Labs-and-Pixeltable/raw/main/Spain_on_a_Fork.mp4', 'creator': '@SpainOnAFork'},
        {'video_url': 'https://github.com/josev2046/Video-Question-Answering-with-Twelve-Labs-and-Pixeltable/raw/main/Ricardo_Gorski_Acne_Cure.mp4', 'creator': '@RicardoGorski'},
        {'video_url': 'https://github.com/josev2046/Video-Question-Answering-with-Twelve-Labs-and-Pixeltable/raw/main/Doctor_Eye_Health_Lash_Lift.mp4', 'creator': '@DoctorEyeHealth'}
    ]

    print(f"📥 Auditing {len(test_submissions)} cloud assets via Twelve Labs Pipeline...")
    compliance_table.insert(test_submissions)

    print("\n" + "="*120)
    print(f"{'CREATOR':<17} | {'DECISION':<10} | {'MULTIMODAL INTELLIGENCE'}")
    print("-" * 120)

    results = compliance_table.collect()
    for row in results:
        report = row.get('report', {})
        engine = report.get('tl_engine', 'Unknown Engine')
        policy = report.get('policy_checks', {}).get('status', 'No findings')
        summary = row.get('summary', 'No summary')
        status = row.get('status', 'BLOCK')
        
        icon = "✅" if status == "APPROVE" else "❌" if status == "BLOCK" else "⚠️"
        
        print(f"{row['creator']:<17} | {icon} {status:<8} | 🤖 {engine}")
        print(f"{'':<17} | {'':<10} | 📝 {summary}")
        print(f"{'':<17} | {'':<10} | 🚩 FINDINGS: {policy}")
        print("-" * 120)

if __name__ == "__main__":
    main()
