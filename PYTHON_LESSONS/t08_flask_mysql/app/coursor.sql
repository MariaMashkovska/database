DELIMITER //

CREATE PROCEDURE CreateDynamicDatabases()
BEGIN
    -- Декларуємо змінні для імені бази даних та кількості таблиць
    DECLARE dbName VARCHAR(50);
    DECLARE tableName VARCHAR(50);
    DECLARE tableCount INT;

    -- Курсор для вибору імен зі стовпця name таблиці user_info
    DECLARE cur CURSOR FOR SELECT name FROM user_info;

    -- Встановлюємо кількість баз даних, яку хочемо створити (в даному випадку 9)
    SET @numDatabases = 9;

    -- Встановлюємо лічильник баз даних
    SET @counter = 1;

    -- Відкриваємо курсор
    OPEN cur;

    -- Цикл для обробки записів курсора
    read_loop: LOOP
        -- Зчитуємо ім'я з курсора
        FETCH cur INTO dbName;

        -- Виходимо з циклу, якщо не залишилося баз даних для створення
        IF @counter > @numDatabases THEN
            LEAVE read_loop;
        END IF;

        -- Генеруємо випадкову кількість таблиць (від 1 до 9) для кожної бази даних
        SET tableCount = FLOOR(RAND() * 9) + 1;

        -- Лічильник таблиць
        SET @tableCounter = 1;

        -- Цикл для створення таблиць
        create_table_loop: LOOP
            -- Задаємо ім'я таблиці, враховуючи порядковий номер
            SET tableName = CONCAT(dbName, '_table_', @tableCounter);

            -- Генеруємо та виконуємо SQL-запит для створення таблиці
            SET @sql = CONCAT('CREATE TABLE IF NOT EXISTS ', tableName, ' (id INT)');
            PREPARE stmt FROM @sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;

            -- Збільшуємо лічильник таблиць
            SET @tableCounter = @tableCounter + 1;

            -- Виходимо з циклу, якщо створено достатню кількість таблиць
            IF @tableCounter > tableCount THEN
                LEAVE create_table_loop;
            END IF;
        END LOOP;

        -- Збільшуємо лічильник баз даних
        SET @counter = @counter + 1;
    END LOOP;

    -- Закриваємо курсор
    CLOSE cur;
END //

DELIMITER ;