# 10. DevOps Deployment Approval System
# Take:
# •	test coverage percentage
# •	security scan status
# •	code review status
# •	environment type
# Rules:
# •	Production deployment allowed only if all checks pass
# •	Staging may allow warning-based deployment
# •	Reject if security scan fails
# •	Conditional approval if review pending but environment is development

test_coverage = float(input("Enter Test Coverage Percentage: "))
security_scan = input("Enter Security Scan Status (pass/fail): ").lower()
code_review = input("Enter Code Review Status (approved/pending): ").lower()
environment = input("Enter Environment (production/staging/development): ").lower()

if security_scan == "fail":
    print("Deployment Status : Rejected")
    print("Reason : Security scan failed.")

elif environment == "production" and test_coverage >= 80 and security_scan == "pass" and code_review == "approved":
    print("Deployment Status : Approved")
    print("Reason : All checks passed for production deployment.")

elif environment == "staging" and security_scan == "pass":
    print("Deployment Status : Approved with Warning")
    print("Reason : Staging environment allows warning-based deployment.")

elif environment == "development" and code_review == "pending":
    print("Deployment Status : Conditional Approval")
    print("Reason : Code review is pending, but deployment is allowed in development.")

else:
    print("Deployment Status : Rejected")
    print("Reason : Deployment conditions not satisfied.")
