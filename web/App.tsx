import { useState } from 'react';
import { View, Text, Pressable, ScrollView, TextInput, Image, Alert } from 'react-native';
import './global.css';

export default function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!username || !password) {
      Alert.alert("ошибка", "Заполни оба поля!");
      return;
    }
    if (password.length < 6) {
      Alert.alert('Ошибка', 'Пароль должен быть минимум 6 символов!');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://192.168.0.100:8000/users/add-user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: 3,
          username: username,
          password: password,
        }),
      });
      const data = await response.json();
      if (response.ok) {
        Alert.alert('Успех', 'Пользователь добавлен!');
        setUsername('');
        setPassword('');
      } else {
        Alert.alert('Ошибка', data.detail || 'Что-то пошло не так');
      }
    } catch (error) {
      Alert.alert('Ошибка', "Ошибка в отправке запроса!");
    } finally {
      setLoading(false);
    }
  }

  return (
    <ScrollView className="flex-1 bg-slate-900">
    <View className="flex-1 bg-slate-900 justify-center items-center px-6 py-20">
      <View className='flex flex-col gap-1 mt-10'>
        <Text className="text-white font-semibold text-4xl text-left">Добро пожаловать!</Text>
        <Text className="text-neutral-300 font-semibold text-2xl text-left">Напиши username пользователя, что бы добавить его в базу данных</Text>
        <Text className='text-white font-semibold mt-5'>Введите username</Text>
        <TextInput placeholder='username' value={username} onChangeText={setUsername} editable={!loading} className='bg-white rounded-[10px] p-2 mt-2 font-semibold'>
        </TextInput>
        <Text className='text-white font-semibold mt-3'>Введите пароль</Text>
        <TextInput secureTextEntry={true} value={password} onChangeText={setPassword} editable={!loading} placeholder='пароль' className='bg-white rounded-[10px] p-2 mt-2 font-semibold'>
        </TextInput>
        <Pressable onPress={handleSubmit} disabled={loading} className='bg-slate-800 py-5 rounded-[15px] mt-5 active:bg-slate-600 transition-all duration-200 ease-out'>
          <Text selectable={false} className='text-white text-center font-semibold text-3xl cursor-default'>{ loading ? 'загрузка...' : 'добавить' }</Text>
        </Pressable>
        
        <View className='bg-slate-800 h-1 rounded-[15px] mt-5'></View>
        <Text className='text-white font-semibold text-4xl mt-5'>Поиск по ID</Text>
        <Text className='text-neutral-300 font-semibold text-2xl'>Напишите ID пользователя, что бы его найти!</Text>

        <Text className='text-white font-semibold mt-5'>Введите ID</Text>
        <TextInput placeholder='ID' className='bg-white rounded-[10px] p-2 mt-2 font-semibold'></TextInput>
        <Pressable onPress={handleSubmit} disabled={loading} className='bg-slate-800 py-5 rounded-[15px] mt-5 active:bg-slate-600 transition-all duration-200 ease-out'>
          <Text selectable={false} className='text-white text-center font-semibold text-3xl cursor-default'>{ loading ? 'загрузка...' : 'добавить' }</Text>
        </Pressable>
      </View>
    </View>
    </ScrollView>
  );
}

