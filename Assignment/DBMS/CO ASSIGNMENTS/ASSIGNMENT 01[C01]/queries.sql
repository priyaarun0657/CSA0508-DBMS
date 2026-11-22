-- 1 Open overdue loans
SELECT * FROM LOAN WHERE Status='OPEN' AND ExpiryDate < CURRENT_DATE;
-- 2 Artifacts without condition evidence
SELECT A.ArtifactID, A.Title FROM ARTIFACT A LEFT JOIN CONDITION_REPORT C ON A.ArtifactID=C.ArtifactID WHERE C.ReportID IS NULL;
-- 3 Loan history by lender
SELECT L.LenderID,L.LoanID,L.StartDate,L.ExpiryDate,L.Status FROM LOAN L ORDER BY L.LenderID,L.StartDate;
-- 4 Artifact loan history
SELECT A.ArtifactID,A.Title,LO.LoanID,L.StartDate,L.ExpiryDate FROM ARTIFACT A JOIN LOAN_OBJECT LO USING(ArtifactID) JOIN LOAN L USING(LoanID);
-- 5 Exhibition slots
SELECT E.ExhibitionName,D.SlotNo,D.SlotLabel FROM EXHIBITION E JOIN DISPLAY_SLOT D USING(ExhibitionID);
-- 6 Condition report count
SELECT ArtifactID,COUNT(*) AS ReportCount FROM CONDITION_REPORT GROUP BY ArtifactID;
-- 7 Current open loans
SELECT * FROM LOAN WHERE Status='OPEN';
-- 8 Ownership share check (period-specific validation must be run separately)
SELECT ArtifactID,ValidFrom,SUM(Share) AS TotalShare FROM ARTIFACT_OWNERSHIP GROUP BY ArtifactID,ValidFrom HAVING TotalShare <> 100;
