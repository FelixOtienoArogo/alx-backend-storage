-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	UPDATE users AS usr,
	(SELECT usr.id, SUM(score * weight) / SUM(weight) AS w_average
	FROM users AS usr
	JOIN corrections AS cor ON usr.id = cor.user_id
	JOIN projects AS pro ON cor.project_id = pro.id
	GROUP BY usr.id)
	AS w_apdt
	SET usr.average_score = w_apdt.w_average
	WHERE usr.id = w_apdt.id;
END$$
DELIMITER ;
